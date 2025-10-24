class Person:
    age: int
    name: str

# Write a function that accepts an age, and a list of people, and it returns
# either:
# a) None
# or b) a list of people with the specified age.
# Specifically, it should return None if there are no people with the specified
# age.
def people_with_age(age: int, people: list[Person]) -> Optional[list[Person]]:
    result = []
    for person in people:
        if person.age == age:
            result.append(person)

    if result == []:
        return None

    return result
