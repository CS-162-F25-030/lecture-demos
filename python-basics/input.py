def main() -> None:
    # Standard output is a special file stream that every process has.
    #       A process is a running instance of a program.
    # In most cases, standard output is "linked" to the terminal by default.
    # The print() function just writes stuff to standard output.

    # Standard input is a special file stream that every process has.
    # In most cases, standard input is "linked" to the terminal by default.
    # The input() function reads stuff from standard input.
    favorite_number = float(input('What is your favorite number?: '))

    print(f'Your number, doubled, is {favorite_number * 2}')

if __name__ == '__main__':
    main()
