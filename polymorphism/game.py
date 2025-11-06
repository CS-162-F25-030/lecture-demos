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
    # Upcasting: Type cast an object of a derived class type to one of its
    # ancestor types

    # Monster
    # Vampire
    # Baby vampire

    # Create the player object
    p = Player()

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
    

if __name__ == '__main__':
    main()

