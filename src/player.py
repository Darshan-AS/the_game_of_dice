from enum import Enum


class PlayerState(Enum):
    PLAY = 'PLAY'
    BONUS = 'BONUS'
    SKIP = 'SKIP'
    END = 'END'

    def __str__(self) -> str:
        return self.value


class Player:

    def __init__(self, name: str, score=0, state=PlayerState.PLAY) -> None:
        self.name = name
        self.__score = score
        self.__state = state

    def __repr__(self) -> str:
        return f'Player(id: {self.name}, score: {self.__score}, state: {self.__state})'

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        return self.score < other.score

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.score == other.score and self.state == other.state

    def __hash__(self) -> int:
        return hash(repr(self)) 

    def add_score(self, score) -> None:
        self.__score += score

    @property
    def score(self) -> int:
        return self.__score

    @property
    def state(self) -> PlayerState:
        return self.__state

    @state.setter
    def state(self, s: PlayerState) -> None:
        self.__state = s
