def main() -> None:
    file_name = input('Enter the file name: ')
    try:
        with open(file_name, 'r') as f:
            print('Successfully opened file')
    except FileNotFoundError as e:
        print('Hey! That file doesn\'t exist!')
        

if __name__ == '__main__':
    main()
