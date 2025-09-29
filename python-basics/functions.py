def volume_of_sphere(radius: float) -> float:
    # Function body goes here
    volume = 4 / 3 * 3.141592 * radius ** 3
    return volume

def main() -> None:
    # A function is a reusable block of code. They can have inputs and outputs.
    # To "call" a function simply means to use it
    print(volume_of_sphere(5.0))
    print(volume_of_sphere(3.0))

if __name__ == '__main__':
    main()
