from domains.students import Students
from domains.courses import Courses
from domains.marks import *
from input import *
from output import *
   
# add students 
stu = Students()
read_students_file(stu)
add_students(stu)
stu.show()
students_file(stu)


# add courses 
cou = Courses()
read_course_file(cou)
add_courses(cou)
cou.show()
courses_file(cou)

# marks 
f = frame(stu, cou)
m = Managment(f, cou)
read_mark_file(m)
add_marks(m)
print(m.df)
marks_file(m)
gpa_df = get_gpa(m.df, cou)
print(sort_gpa(gpa_df))

