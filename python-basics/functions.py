# A scope is a region of code in which a symbol is accessible
# In most cases, the scope of a symbol is the scope in which it's created

# Every function in Python has its own scope. 

# Module scope / global scope is the huge implied scope that exists outside
# of all functions

# x = 12 # Global variables. You should avoid this.


# print(volume) # Syntax error. volume is not declared in this scope.

def main() -> None:
    # A function is a reusable block of code. They can have inputs and outputs.
    # To "call" a function simply means to use it
    print(volume_of_sphere(5.0))
    print(volume_of_sphere(3.0))
    
    radius = 1.0
    print(volume_of_sphere(radius))

    # print(volume) # Syntax error. volume is not declared in this scope.

    if x == 5:
        y = 10
    print(y) # This would be legal

def volume_of_sphere(radius: float) -> float:
    # Function body goes here
    volume = 4 / 3 * 3.141592 * radius ** 3
    return volume


if __name__ == '__main__':
    main()
