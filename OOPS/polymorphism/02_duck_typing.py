# If it walk like a duck and quacks like a duck, then its a duck

class Dog:
    def sound(self):
        print("i am a dog")

class Cat :
    def sound(self):
        print("i am a cat")

obj = Dog()
obj2 = Cat()

obj.sound()
obj2.sound()