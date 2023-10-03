class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal constructor called for {self.species}")

class Mammal(Animal):
    def __init__(self, species, sound):
        super().__init__(species)
        self.sound = sound
        print(f"Mammal constructor called for {self.species}")

class Dog(Mammal):
    def __init__(self, species, sound, name):
        super().__init__(species, sound)
        self.name = name
        print(f"Dog constructor called for {self.name}")

class Cat(Mammal):
    def __init__(self, species, sound, name):
        super().__init__(species, sound)
        self.name = name
        print(f"Cat constructor called for {self.name}")

class Bird(Animal):
    def __init__(self, species, wingspan):
        super().__init__(species)
        self.wingspan = wingspan
        print(f"Bird constructor called for {self.species}")

class Eagle(Bird):
    def __init__(self, species, wingspan, name):
        super().__init__(species, wingspan)
        self.name = name
        print(f"Eagle constructor called for {self.name}")

# Create instances of various classes
dog = Dog("Dog", "Woof", "Buddy")
cat = Cat("Cat", "Meow", "Whiskers")
eagle = Eagle("Eagle", 6.0, "Freedom")

# Access attributes
print(f"{dog.name} is a {dog.species} and says '{dog.sound}'.")
print(f"{cat.name} is a {cat.species} and says '{cat.sound}'.")
print(f"{eagle.name} is an {eagle.species} with a wingspan of {eagle.wingspan} feet.")
