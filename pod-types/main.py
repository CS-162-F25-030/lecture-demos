# You can define your own data types in Python. 
# Classes. A class is a custom data type that you define, such that
# variables of that class can contain other variables inside them.

# Convention: Class names should be written in PascalCase
# For now, we're just going to create POD (plain-old-data) types.
class City:
    # Attribute declarations.
    # An attribute is a variable inside a variable. Only Mypy cares about
    # attribute declarations.
    name: str
    population: int


def print_city(city: City) -> None:
    print(f'City name: {city.name}')
    print(f'City population: {city.population}')


def parse_city(line: str) -> City:
    # Suppose line is 'Corvallis,60000'
    # Then tokens will be ['Corvallis', '60000']
    tokens = line.split(',')
    result = City()
    result.name = tokens[0]
    result.population = int(tokens[1])
    return result


def main() -> None:
    cities = []
    with open('cities.csv', 'r') as cities_file:
        first_line = True
        for line in cities_file:
            if first_line:
                first_line = False
                continue
            cities.append(parse_city(line))

    print_city(cities[1])


if __name__ == '__main__':
    main()
