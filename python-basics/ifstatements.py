def main() -> None:
    password = input("What's the password?: ")

    # Suppose the actual password is "abrakadabra"
    
    # Relational operators in Python
    # == equality
    # != not equal to
    # >
    # <
    # >=
    # <=

    # Logical operators in python:
    # or
    # and
    # not

    if password == 'abrakadabra' or password == 'opensesame':
        # if statement body
        print('Good job!')
    elif password == 'admin':
        print('Welcome abord, captain')
    else:
        # Else body goes here
        print('Incorrect password. Please try again!')

    print('Hello')


if __name__ == '__main__':
    main()
