def average(numbers: list[float]) -> float:
    sum_of_numbers = 0.0
    for x in numbers:
        sum_of_numbers += x
    # At this point, we've added all of the numbers to sum_of_numbers
    return sum_of_numbers / len(numbers)

def main() -> None:
    # A list is like an array.
    # A list is a homogeneous (contiguous) sequence of values.
    #   homogeneous: everything in it is of the same type
    my_list = [3.14, 9.81, 2.71]

    # Element: A thing in a list
    # An index is an integer that specifies the position of an element.
    # In python, lists are indexed by zero.
    print(my_list[2])
    my_list[2] = -1.5
    print(my_list[2])

    # To append means to add to the end of
    my_list.append(5.4)

    print(my_list)

    # You can also insert in the middle
    my_list.insert(1, -100.0)

    print(my_list)

    # Suppose you access an element at an out of range index
    # print(my_list[5]) # Crashes, raises IndexError

    # Suppose you want to delete an element in a list
    del my_list[1]

    print(my_list)

    # You can iterate over a list
    for x in my_list:
        print(x)

    av = average(my_list)
    print(f'Average of numbers is: {av}')

    # List comprehensions


if __name__ == '__main__':
    main()
