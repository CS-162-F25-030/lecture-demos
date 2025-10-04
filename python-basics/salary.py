# Parameters:
# Job title. String. 'Software engineer', 'electrical engineer'
# Num of years worked. Integer.

# Return: The expected annual salary
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
    
    return -1

def main() -> None:
    job_title = input('What is your job title?: ')
    years_worked = int(input('How many years have you worked?: '))
    user_salary = salary(job_title, years_worked)
    print(f'Your expected annual salary is {user_salary}')

if __name__ == '__main__':
    main()
