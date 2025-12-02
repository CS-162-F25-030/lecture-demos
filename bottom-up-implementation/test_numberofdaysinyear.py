from numberofdaysinyear import number_of_days_in_year

def test_number_of_days_in_year_returns_366_for_leap_years() -> None:
    # Arrange
    leap_year = 2000

    # Act
    result = number_of_days_in_year(leap_year)

    # Assert
    assert result == 366, 'Error! Leap years should have 366 days.'

def test_number_of_days_in_year_returns_365_for_non_leap_years() -> None:
    # Arrange
    non_leap_year = 2001

    # Act
    result = number_of_days_in_year(non_leap_year)

    # Assert
    assert result == 365, 'Error! Non-eap years should have 365 days.'

