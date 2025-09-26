def main() -> None:
    # An expression is a piece of code with a type and a value
    
    # In Python, there are various primitive types. Here are a few of them:
    #   int (integer):  whole numbers
    #   float (floating point number): A number with a decimal point in it
    #   bool (boolean): True or False value
    #   str (string): A sequence of zero or more characters

    # You can construct "literals" of each of the above types
    # A literal is a hard-coded value

    # An int literal is simply a whole number. 1   -100   0
    # A float literal is simply a number with a decimal point. 3.14    -9.81
    #       3.     0.0
    # A bool literal is simply True or False
    # A string literal is simply text enclosed in quotation marks OR single
    #   quotes

    print(1)
    print(3.14)
    print(True)
    print(False)
    print("Hello")
    print('Hello')

    # Arithmetic operators:
    # +
    # -
    # *
    # /
    # % (remainder after division)
    # ** (exponentiation)
    #   2 ** 5 = 32
    
    print(2 ** 5) # Prints 32
    print(9 % 3) # Prints 0

    print(1 / 2) # Prints 0.5

    # For now, a variable is a named location in memory where a value can be
    # stored and referred to

    # To create a variable, write the name of the variable, then an assignment
    # operator (=), then the value you want it to initially have
    x = 2 ** 5

    print(x) # Prints 32

    # The syntax to change the value of a variable is the exact same
    x = -123

    # The type of a variable cannot change throughout a program
    x = 3.14
    

if __name__ == '__main__':
    main()
