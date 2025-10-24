from typing import Optional

# None and optionals


class Person:
    name: str
    age: int

def age_of_person(name: str, people: list[Person]) -> Optional[int]:
    for person in people:
        if person.name == name:
            return person.age

    # None is a special value with a special type. Its purpose is to indicate
    # the absence of a real, useful value.
    return None
    

# Suppose you want this function to return a list of things, where each
# of those things is either a person or None. How would you do that?
# def some_function() -> list[Optional[Person]]

# If the goal was to return a value that's either a list of people or None
# Optional[list[Person]]

# If the goal was to return a value that's either 
# a) None, or
# b) a list of things, where each of those things is either None, or a Person
# Optional[list[Optional[Person]]]

def main() -> None:
    people = [
        Person(),
        Person(),
        Person()
    ]
    people[0].name = 'Joe'
    people[1].name = 'Jane'
    people[2].name = 'Jill'
    people[0].age = 25
    people[1].age = 23
    people[2].age = 27

    user_input = input('Enter the name of the person that you want '
        'to search for: ')

    age = age_of_person(user_input, people)

    if age is None:
        print('Error. Couldn\'t find a person with that name.')
    else:
        print(f'The person\'s age is {age}')

    
    x: Optional[str] = 'World'
    x = None # This is allowed
    x = 'Hello' # This is allowed
    x = None # This is allowed
    # x = 1 # This is not

if __name__ == '__main__':
    main()
