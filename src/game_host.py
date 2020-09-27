from game_of_dice import GameOfDice
from player import PlayerState
from die import Die
from pyfiglet import Figlet


class GameHost:
    INTRO_MESSAGE = 'Welcome to the Game of Dice'
    OUTRO_MESSAGE = 'Thank you!'

    def __init__(self) -> None:
        self.figlet = Figlet()

    def show_intro(self) -> None:
        print(self.figlet.renderText(GameHost.INTRO_MESSAGE))
        print(open('assets/rules.txt').read())
    
    def show_outro(self) -> None:
        print(self.figlet.renderText(GameHost.OUTRO_MESSAGE))

    def run(self) -> None:
        player_count = int(input('How many are playing? '))
        win_score = int(input('What is the winning score? '))
        print('\n')

        game = GameOfDice(player_count, win_score)
        while not game.is_game_over():
            player = game.current_player()
            while input(f"{player}. It's your turn now. (Press 'r' to roll the die): ").lower() != 'r':
                pass

            score, player = game.play()

            print()
            Die.show_die(score)
            print()

            print(f'You rolled a {score}')
            if player.state == PlayerState.END:
                print(
                    f'Congrats! You finished at rank {game.get_rank(player)}')
            elif player.state == PlayerState.BONUS:
                print('Awesome! You earned a bonus round :)')
            elif player.state == PlayerState.SKIP:
                print('Bummer! You skip next round :(')

            print()
            game.show_rank_table()
            print('\n' * 3)

        print('Game Over!' + '\n')

def show_contact_info():
    print(open('assets/contact_info.txt').read())

if __name__ == '__main__':
    host = GameHost()
    host.show_intro()
    host.run()
    host.show_outro()
    show_contact_info()
