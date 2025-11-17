def main() -> None:

    # Arrays are basically like Python's lists
    l = [15, -14, 12, 21, 101, 15]

    # Index-based lookup means "find the element with this index"
    print(l[5])

    # Sets are collections of unique data. Also, sets are non-sequential.
    # You can think of sets as "bags of unique data". Sets are very
    # fast at value-based lookups.

    # Value-based lookup means "find the element with this value".
    # "Check whether the given value exists in the collection".

    my_set: set[int] = set()

    my_set.add(12)

    if 101 in l:
        print('101 is in the list!')

    if 101 in my_set:
        print('101 is in the set!')

    # A dictionary maps keys to values
    # Suppose I want to write a program that keeps track of various information
    # about people. And I want to be able to look up a person with a certain
    # name.
    
    people = {
        'John Smith': Person('John Smith', 27, 'Spot'),
        'Sally Smith': Person('Sally Smith', 28, 'Spot')
    }

    print(people['John Smith'].age)
    

if __name__ == '__main__':
    main()
