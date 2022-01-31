<div align="center">

<img src="Images/codeup_logo.png" alt="Codeup Logo" title="Codeup Logo" width="226" height="86" align="center"/>      

# README

### by Sophia Stewart & Jeanette Schulz 
### 31 January 2022


</div align="center">
    
<hr style="border:2px solid blue"> </hr>

# Project Description
### What Is Codeup?
Codeup is a bootcamp that includes gaining the technical knowledge and skillset of a web developer or data scientist, expert instruction, hands-on curriculum with a portfolio to show employers, a close family of your Codeup classmates, a network of technology professionals to connect with, career preparation, continuing job search support even after you graduate, and the peace of mind that if you don’t get hired within 6 months of graduating, you’ll get your tuition back (codeup.com/refund). We also offer a great Return on Investment, one of the best you’ll find.
  
### What is this about?
Although Codeup is a well awarded boot camp for its alumni sucess, it does so by creating a throughly vetted curriculum that is constantly updated. Students only have access to these curriculum websites via thier student emails, which helps to prevent or minimize possible web scraping attempts to this prestigious curriculum. Codeup keeps a database of log entries to both thier web development curriculum and thier data science curriculum. By analyzing these logs, we hope to find out if there have been any web scraping attempts, which lessons are perhaps most read by students, and which lessons alumni refer to after graduation. 


<hr style="border:2px solid blue"> </hr>

# Project Goal
Using the Codeup mySQL database on curriculum log entries, we hope to learn if there have been any web scraping attempts, which lessons are most read by students, and which lessons alumni refer to after graduation. We will then deliver a repository of our work and a single slide of our findings to be inserted in other presentations. 



<hr style="border:2px solid blue"> </hr>

# Project Planning
## Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

<b>Planning:</b>  
- Make sure the data is accessible
- Create a repository to save all our work
- Write a README file with a plan (check!)

<b>Acquisition </b>  
- Collect the data through Codeup's mySQL server
- Create a `wrangle.py` file to make future acquisition easier

<b>Preparation</b>  
- Organize our repository for easy navigation
  - Images directory to hold all photos used
  - Scrapbook directory to hold all work done

<b>Exploration and Pre-processing</b>  
- Explore data to find answers to the questions asked
- Summarize takeaways and conclusions

<b>Modeling</b>  
- There will be no modeling on this data

<b>Deliver</b>  
- A `Final_Report.ipynb` to explain our findings and results.
- A single presentation slide with our findings summarized

<hr style="border:2px solid blue"> </hr>

# Data Dictionary

| Feature                    | Datatype               | Description                                                           |
|:---------------------------|:-----------------------|:----------------------------------------------------------------------|
| date                       | 847330 non-null: object  | log date             |
| time                       | 847330 non-null: object  | log time                  |
| path                       | 847330 non-null: object  | page accessed       |
| ip                         | 847330 non-null: object  | ip address of user access |
| user_id                    | 847330 non-null: int64   | id of the student logging in |
| name                       | 847330 non-null: object  | name of Cohort  |
| program_id                 | 847330 non-null: int64   | id of the program (web dev vs data science)|
| start_date                 | 847330 non-null: object  | date a student started the curriculum  |
| end_date                   | 847330 non-null: object  | date a student finished the curriculum |
<hr style="border:2px solid blue"> </hr>

# Steps to Reproduce

To run the `Final_Report.ipynb` notebook on your own computer you will need to:

 1. Read this README.md (check!)
 3. Download the whole repository 
 4. Copy your own env.py file into the repository 
 8. Run the `Final_Report.ipynb` in a jupyter notebook

<hr style="border:2px solid blue"> </hr>


# Questions we hope to answer for this Project:

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?
