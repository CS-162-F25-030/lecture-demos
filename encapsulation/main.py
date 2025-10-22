from person import Person
from persondatabase import PersonDatabase

def main() -> None:
    joe = Person('Joe', 42)
    mohammad = Person('Mohammad', 24)

    person_database = PersonDatabase()

    # We want to add joe and mohammad to the person database
    person_database.add_person(joe)
    person_database.add_person(mohammad)

    # There is a way to enforce encapsulation: information hiding.
    # In most OOP languages, private attributes are "truly private".
    # In Python, private attributes are not REALLY private.
    # Some people say that in Python, there are no locks on the doors.
    # In this course, do NOT do this.
    # person_database._people.append(joe)



if __name__ == '__main__':
    main()
