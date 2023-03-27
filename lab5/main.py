from domains.students import Students
from domains.courses import Courses
from domains.marks import *
from input import *
from output import *
import os
   
# add students 
stu = Students()
if (os.path.exists("students.txt")):
    try:
        with open('students.txt', 'r') as f:
            list = f.readlines()
            for line in list:
                id, name, dob = line.split(",")
                stu.add_info(id, name, dob)
            f.close()
    except Exception as e:
        print(e)  
input_students(stu)
students_file(stu)

# add courses 
cou = Courses()
if (os.path.exists("courses.txt")):
    try:
        with open('courses.txt', 'r') as f:
            list = f.readlines()
            for line in list:
                id, name, credit = line.split(",")
                credit = float(credit)
                stu.add_info(id, name, credit)
            f.close()
    except Exception as e:
        print(e)     
input_courses(cou)
courses_file(cou)

# marks 
f = frame(stu, cou)
m = Managment(f, cou)
if (os.path.exists("marks.txt")):
    try:
        with open('marks.txt', 'r') as f:
            list = f.readlines()
            for line in list:
                line = line.split(",")
                for i in range(len(m.df.index)):
                    for j in range(len(line)):
                        m.df[j].iloc[i] = line[j]
            f.close()
    except Exception as e:
        print(e)
input_marks(m)
marks_file(m)

