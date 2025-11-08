from player import Player
from zombie import Zombie
from vampire import Vampire
from goblin import Goblin
from monster import Monster

# Polymorphism: "Many forms". A variable that can take on one of many types.
# We're specifically doing subtype polymorphism.

# This function is the main "game loop". In other words, it contains
# the loop that runs the monsters' turns over and over again until the
# game ends (i.e., until the player loses)
def game_loop(
        p: Player,
        monsters: list[Monster]) -> None:
    # Until the player loses, keep running turns of the game
    turn_counter = 1 # Keeps track of what turn it is
    while p.get_hp() > 0:
        # The monsters attack the player
        for m in monsters:
            m.attack(p)

        # Print the player's remaining HP
        print(f"After turn {turn_counter}, the player's remaining "
            f"HP is {p.get_hp()}")
        
        # Update the turn counter
        turn_counter += 1


def main() -> None:
    # Explicit type casting. This takes an object of one type and produces
    # a new object of another type with a "similar" value
    print(int(3.14))

    # Implicit type casting. This is just where you take an object of one
    # type and store it in a variable of another type. This isn't always
    # allowed. This is allowed if and only if the two types are "compatible"

    #x = 3.14
    #x = 5 # This is an example of implicit type casting

    #print(type(x))

    # Upcasting: Type cast an object of a derived class type to one of its
    # ancestor types

    # Monster
    # Vampire
    # Baby vampire

    # Create the player object
    p = Player()

    # The real rule is this. Every variable has two types.
    # 1. A static type. A static type of a variable is its type as can be
    #       inferred by just looking at the code.
    # 2. A dynamic type. A dynamic type of a variable is the actual type
    #       of the actual object that it refers to at a given point in time
    #       during runtime.
    # Static types are not allowed to change. Dynamic types are allowed to
    # change so long as they are always compatible with the static type.

    # Suppose we want the game to have 3 zombies, 4 vampires, and 5
    # goblins. Let's create a list for each (we should use list
    # comprehensions in practice, but they're beyond the scope of
    # this course):
    monsters: list[Monster] = []
    for _ in range(3):
        monsters.append(Zombie()) # This is also an example of upcasting. Implicit upcasting.

    for _ in range(4):
        monsters.append(Vampire())

    for _ in range(5):
        monsters.append(Goblin())

    # Now run the game loop, executing turns until the game is over
    game_loop(p, monsters)
    
    # Abstract classes cannot be instantiated.
    # I cannot create Monster objects anymore.


if __name__ == '__main__':
    main()

