from random import randint


class Die:

    def roll(self) -> int:
        return randint(1, 6)
