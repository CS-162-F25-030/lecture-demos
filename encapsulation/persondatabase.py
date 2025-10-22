from person import Person

class PersonDatabase:
    # Pick an attribute that you want to be encapsulated.
    # Rename it with a leading underscore
    # An attribute that starts with an underscore is said to be "private".
    # Private attributes should only be accessed by methods of the class
    # in which they're declared.
    _people: list[Person] # One day, I might need to replace this with a dict

    def __init__(self) -> None:
        self._people = []

    def add_person(self, person: Person) -> None:
        self._people.append(person)
