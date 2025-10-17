# An attribute is a thing that every instance of a certain class has.
# Attributes establish "has-a" relationships.

# Attributes are data

# Methods establish "can" relationships. They represent things that instances
#   of a certain class "can do".

# Methods are behaviors

class Dog:
    name: str
    birth_year: int

    # A constructor is a special method that is automatically called on
    # an object the moment it's created. The purpose of a constructor
    # is to "set up" or "initialize" an object.
    def __init__(self, name: str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year


    # Every method must have at least one parameter. The first parameter
    # of the method must be named self. And it doesn't need a type annotation.
    def print(self) -> None:
        print(f'Dog\'s Name: {self.name}')
        print(f'Dog\'s birth year: {self.birth_year}')

# Our goal is to convert this into a method of the Dog class.
# This is a global function. It's defined in global scope.
#def print_dog(dog: Dog) -> None:
#    print(f'Dog\'s Name: {dog.name}')
#    print(f'Dog\'s birth year: {dog.birth_year}')
