# Determines whether a given year is a leap year
def is_leap_year(y: int) -> bool:
    # A leap year occurs every year that's a multiple of 4,
    # except for years that are divisible by 100 but not 400.
    # (Yes, this is a true fact. See the below reference.)
    # https://en.wikipedia.org/wiki/Leap_year

    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return False
        else:
            return True
    else:
        return False # Not divisible by 4

# The strategy of writing code that tests other code is referred to as
# automated software testing.
def main() -> None:
    # An assertion is a line of code that states that a certain condition
    # must be true. If that condition is not true, then an AssertionError
    # is automatically raised.

    assert not is_leap_year(2100),\
        ('Error! 2100 is not a leap year, but '
            'it returned true.')

    assert not is_leap_year(2003),\
        ('Error! 2003 is not a leap year, but '
            'it returned true.')

    assert is_leap_year(2004),\
        ('Error! 2004 is a leap year, but '
            'it returned false.')

# There are tools referred to as testing frameworks.
# We are going to use pytest.


if __name__ == '__main__':
    main()
