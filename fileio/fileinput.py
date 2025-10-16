from typing import TextIO
# File I/O. File input/output.

def extract_ages(people_file: TextIO) -> list[int]:
    ages = []
    first_line = True
    for line in people_file:
        if first_line:
            first_line = False
            continue
        line = line.strip()
        # Body goes here
        # Goal: Extract the person's age from the line
        # string split() method extracts tokens from a string given a
        #   separator
        tokens = line.split(',')
        ages.append(int(tokens[2]))

    return ages


def main() -> None:
    # File input.
    with open('people.csv', 'r') as f:
        ages = extract_ages(f)

    # out here in the main() function body again
    
    print(ages)

if __name__ == '__main__':
    main()
