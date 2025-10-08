from traceback import print_exc

def b() -> None:
    my_list = [True, False, False]

    index = int(input('Enter an index: '))

    try:
        print(my_list[index]) 
        # The try block
    except IndexError as e:
        # Except block
        print('Hello, World!')
        print_exc()

        print(e)
    except ValueError as e:
        print('A value error occurred!')
    
    # Continues here
    print('Goodbye, World!')

def a() -> None:
    b()

def main() -> None:
    a()

if __name__ == '__main__':
    main()
