# Multilevel inheritance (Grandfather -> Father -> Son)


class FactoryKolkata:                   
    def __init__(self, material):
        self.material = material

    def show(self):
        print(f"The material is {self.material}")


class FactoryMumbai(FactoryKolkata):                    
    def __init__(self, material, zip):
        super().__init__(material)
        self.zip = zip

    def show2(self):
        print(f"Number of zips : {self.zip}")


class FactoryBhopal(FactoryMumbai):                    
    def __init__(self, material, zip, pocket):
        super().__init__(material, zip)
        self.pocket = pocket

    def show3(self):
        print(f"Number of pockets : {self.pocket}")


class Details(FactoryBhopal):  
    pass


obj = Details("leather", 3, 2)

obj.show()
obj.show2()
obj.show3()