from copy import deepcopy, copy

class Person:
    name: str

def change_me(p: Person) -> None:
    p.name = 'Joe'

def main() -> None:
    jane = Person()
    jane.name = 'Jane'

    # This creates a variable sally, and it sets it up to refer to the object
    # that jane currently refers to
    sally = deepcopy(jane)

    # The deepcopy function creates deep copies.
    # The copy function creates shallow copies.

    sally.name = 'Sally'

    print(jane.name)

    change_me(deepcopy(jane))
    print(jane.name) # What does this print? This prints Jane.

if __name__ == '__main__':
    main()
