# All circles should ALWAYS have a positive radius.
# Information hiding can help us enforce this (class invariant).
class Circle:
    _diameter: float

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('No! Bad radius!')
        else:
            self._diameter = radius * 2

    # Getters are methods that simply return a copy of a private attribute
    # within the object
    def get_radius(self) -> float:
        return self._diameter / 2
    
    # Setters are methods that receive a value as a parameter, and they
    # copy that value into one or more of the private attributes of the
    # object
    def set_radius(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('No! Bad radius!')
        else:
            self._diameter = radius * 2

# Having a private attribute with getters and setters is not VERY different
# from just making the attribute public. Getters and setters sort of "undo"
# the benefits of information hiding. For this reason, you should only create
# getters and setters when you "need" them.

# (But it is a little different).

def main() -> None:
    try:
        c = Circle(-1000.0)
    except ValueError as e:
        print(e)

    c = Circle(10)
    c.set_radius(5)
    print(c.get_radius())
    

if __name__ == '__main__':
    main()
