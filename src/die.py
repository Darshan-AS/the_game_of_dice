from random import randint
from enum import Enum


class Die:
    MIN_VALUE = 1
    MAX_VALUE = 6

    def roll(self) -> int:
        return randint(Die.MIN_VALUE, Die.MAX_VALUE)

    class Pattern(Enum):
        ZERO = "|       |"
        ONE_MID = "|   O   |"
        ONE_LEFT = "| O     |"
        ONE_RIGHT = "|     O |"
        TWO = "| O   O |"
        BORDER = "+-------+"

        def __str__(self) -> str:
            return self.value

    VALUE_PATTERN = {
        1: (Pattern.BORDER, Pattern.ZERO, Pattern.ONE_MID, Pattern.ZERO, Pattern.BORDER),
        2: (Pattern.BORDER, Pattern.ONE_RIGHT, Pattern.ZERO, Pattern.ONE_LEFT, Pattern.BORDER),
        3: (Pattern.BORDER, Pattern.ONE_LEFT, Pattern.ONE_MID, Pattern.ONE_RIGHT, Pattern.BORDER),
        4: (Pattern.BORDER, Pattern.TWO, Pattern.ZERO, Pattern.TWO, Pattern.BORDER),
        5: (Pattern.BORDER, Pattern.TWO, Pattern.ONE_MID, Pattern.TWO, Pattern.BORDER),
        6: (Pattern.BORDER, Pattern.TWO, Pattern.TWO, Pattern.TWO, Pattern.BORDER)
    }

    @classmethod
    def show_die(cls, value: int) -> None:
        if value not in Die.VALUE_PATTERN:
            print('Invalid value for the die')
            return
        
        print(*Die.VALUE_PATTERN[value], sep='\n')
