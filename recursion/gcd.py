# GCD: Greatest common divisor

# a: 64
# b: 24
# c: 48
# The GCD is 8

def gcd(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError('a and b must both be positive!')

    if a < b:
        tmp = a
        a = b
        b = tmp

    # Euclid's Algorithm
    if a % b == 0:
        return b

    return gcd(b, a % b)



def main() -> None:
    print(gcd(64, 24))
    print(gcd(72, 24))
    print(gcd(56, 24))
    

if __name__ == '__main__':
    main()
