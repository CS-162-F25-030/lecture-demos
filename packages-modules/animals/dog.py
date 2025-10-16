class Dog:
    name: str
    birth_year: int

def print_dog(dog: Dog) -> None:
    print(f'Dog\'s Name: {dog.name}')
    print(f'Dog\'s birth year: {dog.birth_year}')
