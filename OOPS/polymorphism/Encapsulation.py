'''There are 3 types of encapsulation
    1. Public Attribute and Methods 
    2. Protected Attributes and Methods
    3. Private Attributes and methods
    '''

class Student:
    def __init__(self):
        self.name = "rahul"             #Public 
        self._age = 20                  #protected
        self.__selary = 100000          # privaye (We can't access it)

obj = Student()

print(obj.name)
print(obj._age)
#print(obj.__selary)  # it shows an error we can't access it directly

