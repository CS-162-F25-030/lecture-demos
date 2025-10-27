class Dog:
    age: int

# "Is-a" relationships
class Husky(Dog):
    # You can put some more stuff in here

def main() -> None:
    h = Husky()
    h.age = 12


if __name__ == '__main__':
    main()
