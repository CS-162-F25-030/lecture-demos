class Cat:
    name: str
    birth_year: int

def print_cat(cat: Cat) -> None:
    print(f'Cat\'s Name: {cat.name}')
    print(f'Cat\'s birth year: {cat.birth_year}')
