import pandas as pd

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