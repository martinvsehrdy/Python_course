from copy import copy


class Dog:
    # class attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __repr__(self):
        return f"{self.name}({self.age})"

    def run(self, minutes=10):
        print(f"{self.name} is running for {minutes} minutes")

    def _eat(self, food):
        print(f"{self.name} eats {food}")

    @classmethod
    def older_than(cls, dog):
        return cls(dog.name, dog.age + 1)

    @staticmethod
    def func():
        pass


dog1 = Dog("alik", 1)
dog2 = Dog("max", 3)

dog3 = copy(dog1)
dog3.name = "Haf"

print(Dog.older_than(dog1))


print(f"dog1 {id(dog1)} {dog1}")
print(f"dog2 {id(dog2)} {dog2}")
print(f"dog3 {id(dog3)} {dog3}")


print(dog1 <= dog2)

