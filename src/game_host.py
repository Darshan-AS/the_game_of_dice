from game_of_dice import GameOfDice
from player import PlayerState


class GameHost:

    @classmethod
    def run(cls):
        player_count = int(input('How many are playing? '))
        win_score = int(input('What is the winning score? '))

        game = GameOfDice(player_count, win_score)
        while not game.is_game_over():
            player = game.current_player()
            while input(f"{player}. It's your turn now. (Press 'r' to roll the die): ").lower() != 'r':
                pass
            score, player = game.play()
            print(f'You rolled a {score}')

            if player.state == PlayerState.END:
                print('Congrats! You finished at rank {rank}!')
            elif player.state == PlayerState.BONUS:
                print('Awesome! You earned a bonus round :)')
            elif player.state == PlayerState.SKIP:
                print('Bummer! You skip next round :(')

            game.show_rank_table()
        print('Game Over!')


if __name__ == '__main__':
    GameHost.run()
