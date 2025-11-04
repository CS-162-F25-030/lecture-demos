from dog import Dog
from sled import Sled

# The answer is inheritance.

# This establishes a parent-child relationship between the Dog class
# and the Husky class.

# In this case, the Dog class is:
# - The parent class
# - The base class
# - The superclass

# In this case, the Husky class is:
# - The child class
# - The derived class
# - The subclass

# What does this DO? Well, it makes it so that the Husky class has every
# attribute and method that the Dog class has. This is automatic.

# Inheritance sort of establishes "is-a" relationships.

# A child class "inherits" all attributes and methods from its parent.
class Husky(Dog):
    # The child class CAN declare / define extra attributes and
    # methods here. This is known as "Extension".

    _energy: int


    # Every husky has TWO __init__ methods
    def __init__(self, owners_name: str, name: str) -> None:
        # The goal is to initialize this husky's _name attribute
        # This will call the derived class's __init__ method
        super().__init__(owners_name, name)
        self._energy = 100

    def pull_sled(self, sled: Sled) -> None:
        if self._energy > 50:
            sled.distance_traveled += 10 # The husky pulled the sled 10 miles
            self._energy -= 10

    # Here, we can override the inherited vocalize() method.
    # What that means is that we define ANOTHER method named vocalize()
    # with the same parameter types and return type.
    def vocalize(self) -> None:
        # This method can do whatever we want it to do. This is the override.
        print('Awooo!')

    def print(self) -> None:
        # Here, we can print ALL the attributes of the husky
        # We can call one of self's methods that it inherited from the Dog
        # class that simply prints its name to the terminal
        super().print() # This calls the Dog class print method() on self
        print(f'Energy: {self._energy}')
