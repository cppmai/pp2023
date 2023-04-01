from domains.__init__ import Info

# Student: __id, __name, __dob  
class Student(Info):
    def __init__(self, id, name, dob):
        super().__init__(id, name)
        self.__dob = dob
    def get_dob(self):
        return self.__dob
    
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
