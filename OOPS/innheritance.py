class Father:
    def house(self):
        print("3 BHK house.")
    def car(self):
        print("A swift car.")

class Son(Father):
    pass

ram = Son()
ram.house()
ram.car()