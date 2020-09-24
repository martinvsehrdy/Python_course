# Parent class
class Pet:
    num = 0
    lastpet = None
    def __init__(self):
        Pet.num += 1
        Pet.lastpet = self
        print("called Pet.__init__")

    def eats(self):
        print("eats")

    @classmethod
    def lastPet(cls):
        return cls.lastpet


# Child class (inherits from Pet class)
class Dog(Pet):
    def __init__(self):
        super().__init__()
        print("called Dog.__init__")


    def haf(self):
        print("haf")


# Child class (inherits from Pet class)
class Cat(Pet):
    def mnau(self):
        print("mnau")

print(Pet.num)
pets = []
pets.append(Dog())
pets.append(Cat())
pets.append(Dog())
print(Pet.num)
print(pets)
print(Pet.lastPet())
c = Cat()
print(c)
print(Pet.lastPet())

