class Person:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age


me = Person("Peter", 25)
you = Person("John", 44)

print(me.species)
print(you.species)