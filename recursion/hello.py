# More formally, recursion is self-dependency

# Recursion: When a function calls itself

def hello_world(counter: int) -> None:
    print('Hello, World!')
    if counter < 9:
        hello_world(counter + 1) # This is a recursive call

def main() -> None:
    hello_world(0)

if __name__ == '__main__':
    main()
