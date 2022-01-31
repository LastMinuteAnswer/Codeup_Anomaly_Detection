import pandas as pd
import numpy as np

def get_url(db):
    '''
    This function takes in a database name and returns a url (using the specified 
    database name as well as host, user, and password from env.py) for use in the 
    pandas.read_sql() function.
    '''
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def acquire_logs():
    '''
    This function first searches for a .csv file containing the curriculum access
    data and then reads that file into a dataframe. If a .csv is not found, it uses
    the get_url() helper function to access the SQL server and read the query result 
    into a dataframe. It then caches this data into a csv file. This function takes 
    no arguments and returns a dataframe.
    '''
    import os
    if os.path.isfile('curriculum_logs.csv'):
        logs = pd.read_csv('curriculum_logs.csv', index_col=0)
        return logs
    else:
        sql = '''
        SELECT date, time, path, ip, user_id, name, program_id, start_date, end_date
        FROM logs
        JOIN cohorts ON logs.cohort_id = cohorts.id;
        '''
        logs = pd.read_sql(sql, get_url('curriculum_logs'))
        logs.to_csv('curriculum_logs.csv')
        return logs

def prep_logs(logs):
    '''
    This function takes in the curriculum access logs dataframe from acquire_logs() and
    converts the access date and time columns to datetime objects and sets that as the index.
    It also adds a column for the name of the programs.
    '''
    # change index to datetime using date and time columns 
    logs = logs.set_index(pd.to_datetime(logs.date + ' ' + logs.time)).drop(columns=['date', 'time'])
    # create column for program names
    logs['program_name'] = logs.program_id.replace([1, 2, 3, 4], ['WebDev-PHP', 'WebDev-Java', 'DataSci', 'FrontEnd'])
    return logs

def wrangle_logs():
    '''
    This function acquires and prepares the curriculum access logs data.
    '''
    return prep_logs(acquire_logs())

def s_wrangle():
    '''
    This function takes no arguments and prepares the curriculum log data for exploration
    to answer my half of the questions.
    '''
    student_logs = wrangle_logs()
    student_logs = student_logs[(student_logs.name != 'Staff') & (~student_logs.path.isin(['/', 'appendix', 'appendix/further-reading', 'toc']))]
    student_logs.dropna(inplace=True)
    student_logs['split_path'] = student_logs.path.str.split('/')
    student_logs['module'] = [lst[0] for lst in student_logs.split_path]
    # get sub-path for each content log
    content = student_logs[student_logs.module == 'content']
    content['cont_mod'] = [av[1] for av in content.split_path]
    # get sub-path for each appendix log
    appendix_views = content[content.module == 'appendix']
    appendix_views['ap_mod'] = [av[1] for av in appendix_views.split_path]
    # drop further-reading main page access logs
    ap_further_reading = appendix_views[(appendix_views.ap_mod == 'further-reading') & (appendix_views.path != 'appendix/further-reading')]
    # get sub-paths for each further-reading log within the appendix
    ap_further_reading['fr_mod'] = [fr[2] for fr in ap_further_reading.split_path]
    # add sub-path columns to curriculum access logs
    merged = pd.merge(student_logs, ap_further_reading[['cont_mod', 'ap_mod', 'fr_mod']], how='left', left_index=True, right_index=True)
    # combine columns
    merged['lesson'] = np.where(merged.cont_mod.isnull(), merged.module, merged.cont_mod)
    merged['lesson'] = np.where(merged.ap_mod.isnull(), merged.lesson, merged.ap_mod)
    merged['lesson'] = np.where(merged.fr_mod.isnull(), merged.lesson, merged.fr_mod)
    # drop unnecessary columns
    merged.drop(columns=['module', 'cont_mod', 'ap_mod', 'fr_mod', 'split_path'], inplace=True)
    merged = merged[~merged.lesson.isin(['appendix', 'content', 'further-reading'])]
    return merged