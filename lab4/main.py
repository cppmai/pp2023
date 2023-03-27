from domains.students import Students
from domains.courses import Courses
from domains.marks import *
from input import *
from output import *

# add students 
stu = Students()
input_students(stu)
show_students(stu)

# add courses 
cou = Courses()
input_courses(cou)
show_courses(cou)

# marks 
f = frame(stu, cou)
m = Managment(f, cou)
input_marks(m)
show_gpas(m)

