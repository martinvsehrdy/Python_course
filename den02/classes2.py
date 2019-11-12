# Parent class
class Pet:
    number_of = 0
    number_of_pets = {}

    def __init__(self):
        Pet.number_of += 1
        print("Creating object of ", self.__class__)
        Pet.number_of_pets[self.__class__] = \
            Pet.number_of_pets.get(self.__class__, 0) + 1

    def eats(self):
        print("eats")

# Child class (inherits from Pet class)
class Dog(Pet):
    def __init__(self):
        print("Creating new Dog")
        super(Dog, self).__init__()


    def haf(self):
        print("haf")

    def eats(self):
        print("I am on diet")
        super(Dog, self).eats()


# Child class (inherits from Pet class)
class Cat(Pet):
    def mnau(self):
        print("mnau")


print(Pet.number_of)

alik = Dog()

alik.eats()

Cat()
Cat()

print(alik.number_of)
print(Pet.number_of)
print(Dog.number_of)
print(Pet.number_of_pets)
