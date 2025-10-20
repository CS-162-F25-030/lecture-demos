from person import Person
from persondatabase import PersonDatabase

def main() -> None:
    joe = Person('Joe', 42)
    mohammad = Person('Mohammad', 24)

    person_database = PersonDatabase()

    # We want to add joe and mohammad to the person database
    person_database.add_person(joe)
    person_database.add_person(mohammad)


if __name__ == '__main__':
    main()
