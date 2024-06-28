
dog_breeds = list()    #  List dog_breeds = new List(); 

dog_breeds.append("Jack Russell")
dog_breeds.append("English Shepherd")
dog_breeds.append("Irish Wolfhound")
dog_breeds.insert(2, "Papillion")
print(f"{dog_breeds = }\n")
print(f"{type(dog_breeds) = }")
print()

class Animal:  # inherits from object
    def breathe(self):
        print("breathing...")

class Dog(Animal):
    def bark(self):
        print("WOOF!! WOOF!!")

d1 = Dog()
print(f"{type(d1) = }")
d1.bark()
d1.breathe()

print(f"{d1 = }")
