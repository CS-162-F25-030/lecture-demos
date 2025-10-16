# import animals.dog as d
from animals.dog import Dog, print_dog

# Modules and packages

# A module is just a .py file that defines something

def main() -> None:
    # I want to create a Dog variable
    spot = Dog()
    spot.name = 'Spot'
    spot.birth_year = 1999
    print_dog(spot)

if __name__ == '__main__':
    main()
