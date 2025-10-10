# File output: Write data from your program into a file
def main() -> None:
    # 'w' opens it in truncate mode. Overwrite mode.
    # 'a' opens it in append mode.
    with open('out.txt', 'a') as f:
        f.write('Hello, World!\n')
        f.write('Hello, World!\n')

if __name__ == '__main__':
    main()
