class Animals:
    type= "Dog"         # Attribute

    def sound(self):       # Method
        print("Bark!")
#Directly accessing attribute and method using the class

print(Animals.type)     # Access the Attribute
Animals().sound()       # Call the Method

