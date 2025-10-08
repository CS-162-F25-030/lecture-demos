def salary(job_title: str, years_worked: int) -> int:
    if job_title == 'software engineer':
        # Compute the expected annual salary based on their num years
        # worked
        if years_worked <= 3:
            return 100000
        else:
            return 130000
    elif job_title == 'electrical engineer':
        # Compute the expected annual salary based on their num years
        # worked
        if years_worked <= 3:
            return 99000
        else:
            return 131000
    
    # Error codes. These are messy.
    return -1

def main() -> None:
    x = salary('software engineer', 10)

    my_list = [True, False, False]

    # Throws an exception. Specifically an IndexError
    print(my_list[3]) # What does this do? Out of bounds / out of range

    # What is an exception??

    # Every function ends in one of three ways:
    # 1. It reaches the end of its control block (body)
    # 2. It returns a value with the return keyword
    # 3. It can throw an exception

    # An exception is an alternative to a return value.

    # Return values are used to communicate "good outputs". 

    # Exceptions are used to communicate that an error occurred

if __name__ == '__main__':
    main()
