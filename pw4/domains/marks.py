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
    gpas = []
    credits = [] 
    def __init__(self, frame, courses: Courses):
        self.df = frame 

        for i in range(len(courses.courses_list)):
            self.credits.append(courses.courses_list[i].get_credit())

    def add_marks(self):
        n = input('choose a course: ')
        if (n in self.df.columns):
            for i in self.df.index:
                s = int(input(f'{i}:'))
                self.df[n].loc[i] = s
        else:
            print("Don't have this course")
        # print(self.df) 

    def get_gpa(self):
        # self.df = self.df.fillna(0)
        for i in self.df.index: 
            g = np.average(self.df.loc[i].tolist(), weights = self.credits)
            self.gpas.append(g)
        self.df['gpa'] = self.gpas
        print(self.df) 

    def sort_gpa(self): 
        print(self.df.gpa.copy().sort_values(by = 'gpa', ascending = False).index.values.tolist())          
