from domains.students import Students
from domains.courses import Courses
from domains.marks import Managment
import os

# input students  
def add_students(students_store: Students):
    n = int(input("# students: "))
    for i in range(n):
        students_store.add()

def read_students_file(students: Students):
    if (os.path.exists("students.txt")):
        try:
            with open('students.txt', 'r') as f:
                list = f.read().splitlines()
                for line in list:
                    id, name, dob = line.split(",")
                    students.add_info(id, name, dob)
                f.close()
        except Exception as e:
            print(e)    

def students_file(students_store: Students):
    try:
        with open('students.txt', 'w') as f:
            for i in range(len(students_store.students_list)):
                p = students_store.students_list[i]
                f.write(f'{p.get_id()},{p.get_name()},{p.get_dob()}\n')
            f.close()
    except Exception as e:
        print(e)    

# input courses 
def add_courses(courses_store: Courses):
    n = int(input("# courses: "))
    for i in range(n):
        courses_store.add()

def read_course_file(courses: Courses):
    if (os.path.exists("courses.txt")):
        try:
            with open('courses.txt', 'r') as f:
                list = f.read().splitlines()
                for line in list:
                    id, name, credit = line.split(",")
                    credit = float(credit)
                    courses.add_info(id, name, credit)
            f.close()
        except Exception as e:
            print(e) 

def courses_file(courses_store: Courses): 
    try:
        with open('courses.txt', 'w') as f:
            for i in range(len(courses_store.courses_list)):
                p = courses_store.courses_list[i]
                f.write(f'{p.get_id()},{p.get_name()},{p.get_credit()}\n')
            f.close()
    except Exception as e:
        print(e) 
    
# add marks for students   
def add_marks(marks_store: Managment): 
    marks_store.add_marks()

def read_mark_file(marks: Managment):
    if (os.path.exists("marks.txt")):
        try:
            with open('marks.txt', 'r') as f:
                list = f.read().splitlines()
                for i in range(len(list)):
                    line = list[i].split(",")
                    for j in range(len(line)):
                        marks.df.iloc[i,j] = line[j]
                f.close()
        except Exception as e:
            print(e)

def marks_file(marks_store: Managment): 
    try:
        with open('marks.txt', 'w') as f:
            for i in marks_store.df.index:
                m = marks_store.df.loc[i].values.tolist()
                for j in m:
                    if (j == m[-1]):
                        f.write(f'{j}\n')
                    else:
                        f.write(f'{j},')
            f.close()
    except Exception as e:
        print(e) 