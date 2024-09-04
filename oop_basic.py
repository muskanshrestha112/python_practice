class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_age(self):
        return 'My age is', self.age

    def __str__(self):
        return f"My name is {self.name}"


neegan = Person('neegan', 22, 'maitidevi')

print(neegan.get_age())
print(neegan)


class Animal:
    def speak():
        return "Chupapi"
    
class Dog(Animal):
    def speaks():
        return "Bark"

class Cat(Animal):
    def speak():
        return "Cat"

class Hybrid(Cat, Dog):
    def speaks():
        return "Rwar"


aaa = Hybrid           

print(aaa.speak())



#
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
    def get_age(self):
        return 'My age is', self.age
    
    def __str__(self):
        return f"My name is {self.name}"
    
   
class Royal(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age, address)
    
    def is_rich(self):
        return True
    
neegan = Royal('neegan', 25, 'maitidevi')

print(neegan.is_rich())
print(neegan.get_age())