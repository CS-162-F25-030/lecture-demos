# Fibonacci sequence: 0 1 1 2 3 5 8 13 21 34

# Suppose I want to write a function fib where you give it an integer n
# and it returns the nth number of the fibonacci sequence
def fib(n: int) -> int:
    if n <= 0:
        raise ValueError('n must be positive!')

    # A base case is a case wherein the arguments are so "small" that the
    # answer is "obvious", in which case you can simply return that answer
    if n == 1:
        return 0

    if n == 2:
        return 1

    # At some point, we need this function to call itself (twice)
    return fib(n-2) + fib(n-1) # These are the recursive calls

# Recursion is suited well for problems that can easily be solved
# by breaking them down into smaller instances of the same problem.
# You do that repeatedly until the problem instances are so small that
# the answers are "obvious". Those are your base cases.

def main() -> None:
    print(fib(4)) # Should return 2

if __name__ == '__main__':
    main()
