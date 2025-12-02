from isleapyear import is_leap_year

# Test coverage is a measure of how much of the code is being tested by
# one or more automated tests.

# Branch coverage: What percentage of your actual lines of code are executed
# by one or more tests?

# Path coverage: What percentage of possible combinations of branches
# are executed in one or more tests?

# What makes a good test? Generally, it's agreed that a test should test
#   "one behavior" and should be as simple as possible.

# Test-driven development (TDD) is development driven by automated testing.
# TDD is often implemented via the Red, Green, Refactor cycle.
# 1. Identify a behavior that has not yet been implemented for a certain
#   component. Write a test for it. At this point, the codebase is said to
#   be in a "red" state. The test fails!
# 2. Make the smallest changes possible to the component (SUT) so as to
#   satisfy the newly tested behavior WITHOUT breaking existing tests.
#   The codebase is now in a "green" state. All tests pass!
# 3. Zoom out, look at the codebase as a whole, and refactor if necessary.
#   Refactor: Change the code without changing what it does.

# A unit test is supposed to test a single behavior of a single component
def test_is_leap_year_returns_true_for_years_divisible_by_400() -> None:
    # Arrange: Arrange the inputs that are going to be passed to
    # the SUT (system under test)
    year_divisible_by_400 = 2000

    # Act: Perform the action whose behavior you want to test
    result = is_leap_year(year_divisible_by_400)

    # Assert
    assert result,\
        ('Error! 2000 is a leap year, but '
            'it returned false.')

def test_is_leap_year_returns_false_for_years_divisible_by_100_but_not_400() -> None:
    assert not is_leap_year(2100),\
        ('Error! 2100 is not a leap year, but '
            'it returned true.')

def test_is_leap_year_returns_false_for_years_indivisible_by_4() -> None:
    assert not is_leap_year(2003),\
        ('Error! 2003 is not a leap year, but '
            'it returned true.')

def test_is_leap_year_returns_true_for_years_just_divisible_by_4() -> None:
    assert is_leap_year(2004),\
        ('Error! 2004 is a leap year, but '
            'it returned false.')
