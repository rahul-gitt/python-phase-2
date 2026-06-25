# There are 3 types of Methods:
    # 1. Instance Method
    # 2. Class Method
    # 3. Static Method

class Animal:

    def __init__(self, name):
        self.name = name

    def bark(self):                     #Instance method
        print(f"{self.name} is barking.")
        
    @classmethod
    def class_method(cls):              #class method
        print("This is class method")

    @staticmethod
    def static_method():                #static method
        print("This is a static method")

obj = Animal("Cheku")
obj.bark()
obj.class_method()
obj.static_method()