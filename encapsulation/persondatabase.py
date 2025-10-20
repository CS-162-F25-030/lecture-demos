from person import Person

class PersonDatabase:
    people: list[Person] # One day, I might need to replace this with a dict

    def __init__(self) -> None:
        self.people = []

    def add_person(self, person: Person) -> None:
        self.people.append(person)
