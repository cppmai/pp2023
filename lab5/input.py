from domains.students import Students
from domains.courses import Courses
from domains.marks import Managment

# input students  
def input_students(students_store: Students):
    n = int(input("# students: "))
    for i in range(n):
        students_store.add()

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
def input_courses(courses_store: Courses):
    n = int(input("# courses: "))
    for i in range(n):
        courses_store.add()

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
def input_marks(marks_store: Managment): 
    marks_store.add_marks()

def marks_file(marks_store: Managment): 
    try:
        with open('marks.txt', 'w') as f:
            for i in marks_store.df.index:
                m = marks_store.df.loc[i].values.tolist()
                for j in m:
                    if (j == m[-1]):
                        f.write(f'{j}')
                    else:
                        f.write(f'{j},')
            f.close()
    except Exception as e:
        print(e) 