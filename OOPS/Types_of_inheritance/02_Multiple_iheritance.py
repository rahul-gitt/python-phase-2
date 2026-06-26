# Multiple Inheritance (Many Parents and one chield)

class FactoryKolkata:   #PARENT CLASS
    def show(self):
        print("Leather")

class FactoryMumbai:    #PARENT CLASS
    def show2(self):
        print("3 Zips")

class FactoryBhopal:    #PARENT CLASS
    def show3(self):
        print("2 Pockets")

class Details(FactoryBhopal, FactoryMumbai, FactoryKolkata):    #CHIELD CLASS
    pass

obj = Details()

obj.show()
obj.show2()
obj.show3()