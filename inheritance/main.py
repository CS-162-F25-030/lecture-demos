from dog import Dog
from husky import Husky
from sled import Sled

def main() -> None:
    santas_sleigh = Sled()

    spot = Dog('Spot')
    spot.bark()

    fluffy = Husky('Fluffy')
    fluffy.bark()

    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)
    fluffy.pull_sled(santas_sleigh)

    print(f'Santa\'s sleigh has been pulled '
        f'{santas_sleigh.distance_traveled} miles')

if __name__ == '__main__':
    main()
