# Create thebasic structure of OOPS for build understanding

class Factory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"Your object details are {self.material}, {self.zips}, {self.pockets}")
    
reebok = Factory("Leather",3,2)
wrong = Factory("Nylon",4,2)
sky_bags = Factory("Nylon",3,3)
        
reebok.show()

'''Class: Blueprint for creating objects.
Object: Instance of a class.
Constructor (__init__): Initializes object attributes automatically.
self: Refers to the current object.
Method: A function defined inside a class.
Attribute: A variable that belongs to an object.'''