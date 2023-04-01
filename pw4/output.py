from domains.students import Students
from domains.courses import Courses
from domains.marks import Managment

def show_students(students_store: Students):
    students_store.show()

def show_courses(courses_store: Courses):
    courses_store.show() 

def show_gpas(marks_store: Managment):
    marks_store.get_gpa()
    marks_store.sort_gpa()