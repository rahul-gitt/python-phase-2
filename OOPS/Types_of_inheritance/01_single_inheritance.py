# Single Inheritance (one chield class & one parent class)

class Father:
    def home(self):
        print("3 BHK house.")

class Son(Father):
    def car(self):
        print("A scorpio car")

obj = Son()
obj.home()
obj.car()