# Info: __id, __name 
class Info:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name 
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

# Student: __id, __name, __dob  
class Student(Info):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.__dob = dob
    def get_dob(self):
        return self.__dob

# Course: __id, __name    
class Course(Info):
    pass

# Student Managent: list of Student objects 
# students_list = [StudentObj1, StudentObj2, .....] 
class Students:
    students_list = []
    def add(self):
        id = input("student's id: ")
        name = input("student's name: ")
        dob = input("student's dob: ")
        student = Student(id, name, dob)
        self.students_list.append(student)
    def len(self):
        return len(self.students_list)
    def show(self):
        print('ID\tName\tDoB')
        for i in range(len(self.students_list)):
            print('{}\t{}\t{}'.format(self.students_list[i].get_id(), self.students_list[i].get_name(), self.students_list[i].get_dob()))

# Course Managment: list of Course objects
# courses_list = [CourseObj1, CourseObj2, .......] 
class Courses:
    courses_list = []
    def add(self):
        id = input("course's id: ")
        name = input("course's name: ")
        course = Course(id, name)
        self.courses_list.append(course)
    def len(self):
        return len(self.courses_list)
    def show(self):
        print('ID\tName')
        for i in range(len(self.courses_list)):
            print('{}\t{}'.format(self.courses_list[i].get_id(), self.courses_list[i].get_name()))

# Marks Managment: dict of list
# key: course_name
# values: marks of students in a course
class Marks:
    marks = {}
    def __init__(self, students: Students, courses: Courses):
        self.students = students
        self.courses = courses
        for i in range(self.courses.len()):
            self.marks[self.courses.courses_list[i].get_name()] = []  
    def add_mark(self):
        n = input('choose a course: ')
        for i in range(self.students.len()):
            s = float(input('{}: '.format(self.students.students_list[i].get_name())))
            self.marks[n].append(s)
    def show_mark(self):
        n = input('choose a course: ')
        if (len(self.marks[n]) == 0):
            print('marks of course is empty')
        else:
            print('ID\tName\tMarks')
            for i in range(self.students.len()):
                print('{}\t{}\t{}'.format(self.students.students_list[i].get_id(),self.students.students_list[i].get_name(), self.marks[n][i]))


stu = Students()
cou = Courses()

while(True):
  print("""Menu
  1. Input info 
  2. Add marks for a course
  3. Student list
  4. Courses list
  5. Marks list
  6. Exist""")
  c = int(input('Enter your choice: '))
  if (c==1):
    n = int(input("# students: "))
    for i in range(n):
       stu.add()
    n = int(input("# courses: "))
    for i in range(n):
      cou.add()
    m = Marks(stu, cou)
  elif (c==2):
    m = Marks(stu, cou)
    m.add_mark()
  elif (c==3):
    stu.show()
  elif (c==4):
    cou.show()
  elif (c==5):
    m.show_mark()
  elif (c==6):
    break
  else:
    print('Wrong choice!')                  



    
    
        


