from abc import ABC, abstractmethod

from player import Player

# ABC stands for abstract base class. By inheriting from ABC, the Monster
# class is now abstract.
class Monster(ABC):
    _hp: int

    def __init__(self, hp: int) -> None:
        # Different monsters will start out with different amounts
        # of hp, so we pass the monster's starting HP as an argument
        # to this constructor's hp parameter. It then stores it in
        # the self._hp attribute.
        self._hp = hp

    # Abstract methods provide an interface but no implementation
    @abstractmethod
    def attack(self, p: Player) -> None:
        pass
