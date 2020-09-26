from io import UnsupportedOperation
from player import Player, PlayerState
from die import Die
from collections import deque

class GameOfDice:
    GAME_OVER = 'Game Over!'

    def __init__(self, player_count: int, win_score: int) -> None:
        self.player_count = player_count
        self.win_score = win_score
        self.die = Die()
        self.all_players = [Player(f'Player {id_}') for id_ in range(1, player_count + 1)]
        self.players = deque(self.all_players)

    def is_game_over(self) -> bool:
        return len(self.players) == 0

    def current_player(self, pop=False) -> Player:
        if self.is_game_over():
            raise UnsupportedOperation(GameOfDice.GAME_OVER)

        while self.players[0].state == PlayerState.SKIP:
            player = self.players.popleft()
            player.state = self.__find_player_state(player)
            self.players.append(player)
        return self.players.popleft() if pop else self.players[0]

    def play(self) -> tuple:
        if self.is_game_over():
            raise UnsupportedOperation(GameOfDice.GAME_OVER)

        player = self.current_player(pop=True)
        score = self.die.roll()
        player.add_score(score)
        player.state = self.__find_player_state(player, score)

        if player.state == PlayerState.BONUS:
            self.players.appendleft(player)
        elif player.state != PlayerState.END:
            self.players.append(player)

        return score, player

    def __find_player_state(self, player: Player, score=0) -> PlayerState:
        if player.score >= self.win_score:
            return PlayerState.END
        elif score == 6:
            return PlayerState.BONUS
        elif score == 1:
            return PlayerState.SKIP
        else:
            return PlayerState.PLAY

    def show_rank_table(self) -> None:
        print(self.all_players)
