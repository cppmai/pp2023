from domains.students import Students
from domains.courses import Courses
from domains.marks import Managment
import os
import pickle
import pandas as pd

# input students  
def add_students(students_store: Students):
    n = int(input("# students: "))
    for i in range(n):
        students_store.add()

def read_students_file(students: Students):
    if (os.path.exists("students.pickle")):
        file_name = 'students.pickle'
        with open(file_name, 'rb') as file:
            students.students_list = pickle.load(file) 

def students_file(students_store: Students):
    file_name = 'students.pickle'
    with open(file_name, 'wb') as file:
        pickle.dump(students_store.students_list, file)   

# input courses 
def add_courses(courses_store: Courses):
    n = int(input("# courses: "))
    for i in range(n):
        courses_store.add()

def read_courses_file(courses: Courses):
    if (os.path.exists("courses.pickle")):
        file_name = 'courses.pickle'
        with open(file_name, 'rb') as file:
            courses.courses_list = pickle.load(file) 

def courses_file(courses_store: Courses): 
    file_name = 'courses.pickle'
    with open(file_name, 'wb') as file:
        pickle.dump(courses_store.courses_list, file) 
    
# add marks for students   
def add_marks(marks_store: Managment): 
    marks_store.add_marks()

def read_marks_file(marks: Managment):
    df = pd.DataFrame()
    if (os.path.exists("marks.pickle")):
        file_name = 'marks.pickle'
        with open(file_name, 'rb') as file:
            df = pickle.load(file) 
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            marks.df.iloc[i,j] = df.iloc[i,j]

def marks_file(marks_store: Managment): 
    file_name = 'marks.pickle'
    with open(file_name, 'wb') as file:
        pickle.dump(marks_store.df, file)