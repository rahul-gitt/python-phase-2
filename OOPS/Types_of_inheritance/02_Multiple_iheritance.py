# Multiple Inheritance (Many Parents and one chield)

class FactoryKolkata:                   #PARENT CLASS
    def __init__(self,material):
        self.material = material

    def show(self):
        print(f"The material is {self.material}")

class FactoryMumbai:                    #PARENT CLASS
    def __init__(self,material,zip):
        super().__init__(material)
        self.zip = zip

    def show2(self):
        print(f"Number of zips : {self.zip}")

class FactoryBhopal:                    #PARENT CLASS
    def __init__(self,material,zip,pocket):
        super().__init__(material,zip)
        self.pocket = pocket

    def show3(self):
        print(f"Number of pockets : {self.pocket}")

class Details(FactoryBhopal,FactoryMumbai,FactoryKolkata):           #CHIELD CLASS
    pass

obj = Details("leather",3,2)

obj.show()
obj.show2()
obj.show3()