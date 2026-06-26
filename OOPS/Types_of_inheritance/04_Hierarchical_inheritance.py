# Hierarchical Inheritance      (# One parent -> many chield)

class Factory:                      # Parent Class
    def __init__(self, material):
        self.material = material

    def show_material(self):
        print(f"Material: {self.material}")


class Reebok(Factory):              # Child 1
    def show_brand(self):
        print("Brand: Reebok")


class Nike(Factory):                # Child 2
    def show_brand(self):
        print("Brand: Nike")


class Puma(Factory):                # Child 3
    def show_brand(self):
        print("Brand: Puma")


obj1 = Reebok("Leather")
obj2 = Nike("Nylon")
obj3 = Puma("Canvas")

obj1.show_material()
obj1.show_brand()

print()

obj2.show_material()
obj2.show_brand()

print()

obj3.show_material()
obj3.show_brand()