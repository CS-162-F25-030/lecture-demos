def main() -> None:
    x = 3.9999
    y = 1

    # Type casting: Convert an expression of one type into an expression of
    # another type
    # x = float(y)

    # Rule for float to integer type casting is truncation
    y = int(x)

    print(y)

if __name__ == '__main__':
    main()
