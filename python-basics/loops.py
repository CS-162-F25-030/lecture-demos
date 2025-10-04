def main() -> None:
    # Two kinds of loops in Python
    # While loops
    # For loops

    i = 0
    while i < 10:
        a = 1
        # Body goes here
        print(i)
        i += 1
    
    # Examples of iterables: lists, ranges, tuples, dicts
    # A range is a list of whole numbers. Every range has a start, a stop,
    # and a step.
    # If I wanted a range that contained the numbers 1-10, then the start
    # would be 1, and the stop would be 11.
    
    for j in range(10):
        # For loop body goes
        print(j)



if __name__ == '__main__':
    main()
