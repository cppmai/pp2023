from domains.students import Students
from domains.courses import Courses

import numpy as np
import pandas as pd 

# Marks Managment: dataframe
def frame(students: Students, courses: Courses): 
    # Students' info 
    sids = []
    snames = []
    for i in range(len(students.students_list)):
        sids.append(students.students_list[i].get_id())
        snames.append(students.students_list[i].get_name())

    # Courses' info
    cids = []
    cnames = []
    credits = []
    for i in range(len(courses.courses_list)):
        cids.append(courses.courses_list[i].get_id())
        cnames.append(courses.courses_list[i].get_name())
        credits.append(courses.courses_list[i].get_credit())

    df = pd.DataFrame(columns = cnames, index = snames)
    return df

class Managment:
    def __init__(self, frame, courses: Courses):
        self.df = frame 

    def add_marks(self):
        for n in self.df.columns:
            print('Course', n, ':')
            for i in self.df.index:
                if (self.df[n].isnull().loc[i]):
                    s = int(input(f'{i}:'))
                    self.df[n].loc[i] = s 
                else:
                    continue

def get_gpa(df, courses: Courses):
    gpas = []
    credits = [] 
    marks = df.copy()
    for i in range(len(courses.courses_list)):
        credits.append(courses.courses_list[i].get_credit())
  
    for i in marks.index: 
        g = np.average(list(map(int,marks.loc[i].tolist())), weights = credits)
        gpas.append(g)
    marks['gpa'] = gpas
    return marks

def sort_gpa(df): 
    return (df.sort_values(by = 'gpa', ascending = False))          
