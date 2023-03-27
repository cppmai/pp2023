from domains.__init__ import Info

# Course: __id, __name, __credit    
class Course(Info):
    def __init__(self, id, name, credit):
       super().__init__(id, name)
       self.__credit = credit
    def get_credit(self):
       return self.__credit 
    
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
    def add_info(self, id, name, credit):
        course = Course(id, name, credit)
        self.courses_list.append(course)
    def len(self):
        return len(self.courses_list)
    def show(self):
        print('ID\tName\tCredit')
        for i in range(len(self.courses_list)):
            print('{}\t{}\t{}'.format(self.courses_list[i].get_id(), self.courses_list[i].get_name(), self.courses_list[i].get_credit()))
