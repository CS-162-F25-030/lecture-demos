from isleapyear import is_leap_year

def test_is_leap_year_returns_true_for_years_divisible_by_400() -> None:
    assert is_leap_year(2000),\
        ('Error! 2000 is a leap year, but '
            'it returned false.')
