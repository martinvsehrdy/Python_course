import copy


class Dog:
    species = "mammal"
    # Initializer / Instance Attributes
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def hide_bone(self):
        self._where_is_bone = ""

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f"Str Dog {self.name}"

    def __repr__(self):
        return f"Repr Dog {self.name}, {self.age}"

    @classmethod
    def older_then(cls, dog):
        return cls(dog.name, dog.age + 1)


if __name__ == '__main__':
    d = Dog("Alik", 3)
    d.hide_bone()

    older = Dog.older_then(d)

    d2 = copy.copy(d)

    d.species

    r = Dog("Alik", 3)

    print(str(d), r)
    print(d == r)
    d.__eq__(r)

    slovnik = {}
    slovnik[d] = 1
    slovnik[r] = 1

    print(d.name)

    for i in d:
        print(i)


    print(slovnik)

