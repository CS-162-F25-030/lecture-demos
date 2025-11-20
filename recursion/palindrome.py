# Suppose we want to write function that accepts a string s and determines
# whether s is a palindrome or not, returning True if so and False otherwise.

# Palindrome: A string that's the same when read forward and backward

def is_palindrome(s: str) -> bool:
    # A palindrome is a string that satisfies the following two criteria:
    # 1. The first character is equal to the last character
    # 2. Everything in between must be a palindrome

    # Base cases
    if len(s) == 0:
        return True

    if len(s) == 1:
        return True # All strings of length 1 are palindromes

    if s[0] != s[-1]:
        return False

    if not is_palindrome(s[1:len(s)-1]):
        return False

    return True


def main() -> None:
    print(is_palindrome('racecar'))
    print(is_palindrome('raceecar'))
    print(is_palindrome('racefdjsaecar'))
    

if __name__ == '__main__':
    main()
