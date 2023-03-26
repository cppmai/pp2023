import numpy as np
import math 
import pandas as pd 

# class section 
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
    def __init__(self, id, name, credit):
       super().__init__(id, name)
       self.__credit = credit
    def get_credit(self):
       return self.__credit 

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
        credit = int(input('credit: '))
        course = Course(id, name, credit)
        self.courses_list.append(course)
    def len(self):
        return len(self.courses_list)
    def show(self):
        print('ID\tName\tCredit')
        for i in range(len(self.courses_list)):
            print('{}\t{}\t{}'.format(self.courses_list[i].get_id(), self.courses_list[i].get_name(), self.courses_list[i].get_credit()))

# Marks Managment: dataframe
def frame(students: Students, courses: Courses): 
    # Students' info 
    sids = []
    snames = []
    for i in range(len(students.students_list)):
        sids.append(students.students_list[i].get_id())
        snames.append(students.students_list[i].get_name())

    # Courses' info
    cids = []
    cnames = []
    credits = []
    for i in range(len(courses.courses_list)):
        cids.append(courses.courses_list[i].get_id())
        cnames.append(courses.courses_list[i].get_name())
        credits.append(courses.courses_list[i].get_credit())

    df = pd.DataFrame(columns = cnames, index = snames)
    return df

class Managment:
    gpas = []
    credits = [] 
    def __init__(self, frame, courses: Courses):
        self.df = frame 

        for i in range(len(courses.courses_list)):
            self.credits.append(courses.courses_list[i].get_credit())

    def add_marks(self):
        n = input('choose a course: ')
        if (n in self.df.columns):
            for i in self.df.index:
                s = int(input(f'{i}:'))
                self.df[n].loc[i] = s
        else:
            print("Don't have this course")
        print(self.df) 

    def get_gpa(self):
        for i in self.df.index: 
            g = np.average(self.df.loc[i].tolist(), weights = self.credits)
            self.gpas.append(g)
        self.df['gpa'] = self.gpas 
        print(self.df) 

    def sort_gpa(self): 
        print(self.df.gpa.copy().sort_values(ascending = False).index.values.tolist())          

       

stu = Students()
cou = Courses()

# input students  
n = int(input("# students: "))
for i in range(n):
    stu.add()

# input courses 
n = int(input("# courses: "))
for i in range(n):
    cou.add()
    
# add marks for students    
f = frame(stu, cou)
m = Managment(f, cou)
m.add_marks()
m.get_gpa()
m.sort_gpa()

                



    
    
        


