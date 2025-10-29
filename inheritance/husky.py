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

    def __init__(self, name: str) -> None:
        # The goal is to initialize this husky's _name attribute
        super().__init__(name)
        self._energy = 100

    def pull_sled(self, sled: Sled) -> None:
        if self._energy > 50:
            sled.distance_traveled += 10 # The husky pulled the sled 10 miles
            self._energy -= 10
