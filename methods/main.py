from animals.dog import Dog

def main() -> None:
    # I want to create a Dog variable
    spot = Dog('Spot', 1999)
     
    # This is a change in paradigm.
    # We aren't doing something with spot. Instead, we're TELLING spot
    # to do something.
    # This perspective, "Tell Dont Ask", is a cornerstone of "object-oriented
    # programming". OOP is basically programming that's centered around
    # objects.

    # An object is an instance of class.
    spot.print()

    #print_dog(spot)

# An object is:
# Definition 1: An instance of a class
# Definition 2: An instance of a class that has both data and behavior
# Definition 3: In the Python language standard, an object is any value

if __name__ == '__main__':
    main()
