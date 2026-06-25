# There are two types of attribute
# 1. class attribute
# 2. instance attribute

class Car:
    wheels = 4  # class attribute

    def __init__(self,color):   # instance attribute
        self.color = color