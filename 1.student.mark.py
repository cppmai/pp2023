# course
courses = []
def add_courses():
  n = int(input('# courses: '))
  for i in range(n): 
    print('Course '+str(i+1))
    id = input('ID: ')
    name = input('Name: ')
    # 1 dict - 1 course 
    d1 = dict(course_id=id, course_name=name)
    # add 1 course into list 
    courses.append(d1)

def show_courses():
   print('List courses:')
   for i in range(0,len(courses)):
     print(courses[i].get('course_id'),' : ',courses[i].get('course_name'))

# student
students = []
def add_students():
  n = int(input('# students: '))
  for i in range(n):
    print('Student '+str(i+1))
    # student information 
    id = input('ID: ')
    name = input('Name: ')
    dob = input('DoB: ')
    # 1 dict - 1 student 
    d2 = dict(student_id = id, student_name = name, student_dob = dob)
    # add 1 student into list 
    students.append(d2)

def show_students():
  print('List student')
  print('ID\tName\tDob')
  for i in range(len(students)):
    print(students[i].get('student_id'),'\t',students[i].get('student_name'),'\t',students[i].get('student_dob'))

# mark
# merge students and courses list 
mark = []
def student_course():
  # copy list od student information 
  marks = students.copy()
  # add names of courses as keys in a dictionary of each student 
  for i in range(len(students)):
    for j in range(len(courses)):
      marks[i][str(courses[j]['course_name'])]=None 
    mark.append(marks[i])

def input_marks():
  student_course()
  c = input('Enter name of course: ')
  # check if that course exists
  if (c in  mark[0].keys()): 
    for i in range(len(students)):
      print(mark[i]['student_name'],':')
      s = int(input())
      mark[i][c]=s
  else:
    print('Not have this course')

def show_marks(): 
  c = input('Enter name of course: ')
  if (c in  mark[0].keys()): 
    print('ID\tName\t',c)
    for i in range(len(students)):
      print(mark[i]['student_id'],'\t',mark[i]['student_name'],'\t',mark[i][c])
  else:
    print('Not have this course') 

# test
while(True):
  print('Menu\n1.Add students\n2.Add courses\n3.Add marks for a course\n4.Student list\n5.Courses list\n6.Marks list\n7.Exist')
  c = int(input('Enter your choice: '))
  if (c==1):
    add_students()
  elif (c==2):
    add_courses()
  elif (c==3):
    if (len(students)==0 | len(courses)==0):
      print('Lack info of students or courses')
      continue
    else:
      input_marks()
  elif (c==4):
    show_students()
  elif (c==5):
    show_courses()
  elif (c==6):
    show_marks()
  elif (c==7):
    break
  else:
    print('Wrong choice!')



