def main() -> None:
    valid_input = False
    while not valid_input:
        try:
            age = int(input('What is your age?: '))
            if age >= 0:
                valid_input = True
            else:
                print('Hey! Thats negative!')
        except ValueError as e:
            print('Hey! Thats not even a number! Try again.')
        

    
if __name__ == '__main__':
    main()
