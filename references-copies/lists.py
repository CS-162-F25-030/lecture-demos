def change_value(the_list: list[int]) -> None:
    the_list[0] = 100

def main() -> None:
    l = [1, 2, 3, 4, 5]

    change_value(l)

    print(l[0]) # What does this print? 100

if __name__ == '__main__':
    main()
