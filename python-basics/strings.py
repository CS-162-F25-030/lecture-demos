def main() -> None:
    cool_word = 'lightning'

    cool_word = 'thunder' + ' ' + cool_word

    cool_word += ' hello'

    print(cool_word)

    # cool_word = f'{4 + 7 * 2}'

    # Index. Python is indexed by 0.
    print(cool_word[0])

    # In Python, strings are immutable
    # Mutable: Can be changed (mutate)
    # Immutable: Cannot be changed
    # cool_word[0] = 'b'
    

if __name__ == '__main__':
    main()
