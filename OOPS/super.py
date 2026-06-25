# Learning about super function

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Hello the Student name is {self.name} and age is {self.age}")

class Details(Student):
    def __init__(self, name, age,roll,section):
        super().__init__(name,age)
        self.roll = roll
        self.section = section
    def show2(self):
        print(f"The roll no. is {self.roll} and sec is {self.section}")
    

obj = Details("Rahul", 20, 543,"J")
obj.show()
obj.show2()