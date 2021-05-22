# khai báo lớp đới tuiowngj
# class Person:
#     name = "Bình"
# Person.age =10
# del Person.age
# print(Person.age)
#hàm dựng
#magic function
# _name: protected
# __name:private
#property
class Person:
    def __init__(self, name="unknown", age = 1):
        self.__name = name
        self.__age = age
    # def __del__(self):
    #     print("detroyed" ,self.name)
    def get_name(seft):
        return seft.name
    def set_name(seft, name):
        seft.name = name
    def get_age(seft):
        return seft.age
    def set_age(seft, age):
        seft.age = age
    def __str__(self):
        return "name: "+ self.name
    def __call__(self):
        print("Called")
    @property
    def name(seft):
        return seft.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @staticmethod
    def sayHello():
        print("Hello")
    # def func(seft):
    #     pass  qquy định truyền xuống dưới để thg lơp kia sử dụng
class Student(Person):
    def __init__(self, name, age,GPA):
        super().__init__(name,age)
        self.__GPA = GPA
    def get_GPA(self):
        return self.__GPA
# Person1 = Person("Bình", 19)
# Person1.set_name("Linh")
Student1 = Student("Bình", 19,10)
print(Student1.get_name)
print(Student1.get_age)
print(Student1.get_GPA)
