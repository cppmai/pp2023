from domains.students import Students
from domains.courses import Courses
from domains.marks import Managment

# input students  
def input_students(students_store: Students):
    n = int(input("# students: "))
    for i in range(n):
        students_store.add()

# input courses 
def input_courses(courses_store: Courses):
    n = int(input("# courses: "))
    for i in range(n):
        courses_store.add()
    
# add marks for students   
def input_marks(marks_store: Managment): 
    marks_store.add_marks()