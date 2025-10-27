# References and copies / Python object model

def main() -> None:
    # According to the Python language standard, an object is any value.

    # Here's what the assignment operator REALLY does: It
    # creates a variable on the left (if it doesn't already exist). Then,
    # it sets up that variable to REFER to the object on the right.
    x = 5

    # This sets up y to refer to the object that x currently refers to.
    y = x

    # Variables are not actually objects. Variables are REFERENCES to
    # objects.

    # In Python, EVERY object has a unique identifier.
    print(id(x))
    print(id(y))

    x += 12 # Equivalent to x = x + 12
    print(x) # Prints 17
    print(y) # Prints 5

    y = 0


if __name__ == '__main__':
    main()
