# polymorohism 
#Method 1 = Override

class Animal:
    def show(self):
        print("I am an animal")

class Human(Animal):
    def show(self):                     # Override previous show
        print("I am a Human.")     

obj = Human()

obj.show()      # it show only i am a human beacuse it override the I am an animal line.
obj.show()