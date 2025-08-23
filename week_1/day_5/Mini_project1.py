from enum import Enum
import random

class Move(Enum):
    Rock = "r"
    Paper = "p"
    Scissors = "s"

class Player:
    def __init__(self, score = 0, is_computer = False):
        self.score = score
        self.move = None
        self.is_computer = is_computer

    def choose_move(self, move):
        self.move = move

class Game:
    def __init__(self,rounds = 0):
        self.rounds = rounds
        self.player = Player()
        self.computer = Player(is_computer=True)
        self.drew = 0

    def menu(self):
        print("Menu:")
        choice = input("(g) Play a new game\n(x) Show scores and exit: ").strip().lower()

        while choice not in ['g','x']:
            choice = input("Invalid input please choose (g) for new play or (x) to show scores and exit :").strip().lower()

        if choice == 'g':
            self.play()
        else:
            self.score()

    def score(self):
        print("Game results:")
        print(f"\tYou won {self.player.score} times.")
        print(f"\tYou lost {self.computer.score} times.")
        print(f"\tYou drew {self.drew} times.")
        print(f"\nThanks you for playing!")

    def play(self):
        move_map = {"r": Move.Rock, "p": Move.Paper, "s": Move.Scissors}
        try:
            self.rounds = int(input("Enter how many rounds do you want to play?"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.play()

        for i in range(self.rounds):
            print(f"Round {i + 1}:")
            player_input = input("Select (r)ock, (p)aper, (s)cissors: ")
            while player_input not in move_map:
                player_input = input("Invalid move. Please select (r)ock, (p)aper, (s)cissors: ")
            self.player.choose_move(move_map[player_input])

            self.computer.choose_move(random.choice(list(Move)))

            if self.player.move == self.computer.move:
                print(f"You choose {self.player.move.name}. The computer choose {self.computer.move.name}. It's a draw!")
                self.drew += 1
            elif (self.player.move == Move.Rock and self.computer.move == Move.Scissors) or \
                 (self.player.move == Move.Paper and self.computer.move == Move.Rock) or \
                 (self.player.move == Move.Scissors and self.computer.move == Move.Paper):
                print(f"You choose {self.player.move.name}. The computer choose {self.computer.move.name}. You win!")
                self.player.score += 1
            else:
                print(f"You choose {self.player.move.name}. The computer choose {self.computer.move.name}. You lose!")
                self.computer.score += 1

        self.menu()

    @staticmethod
    def start():
        game = Game()
        game.menu()


Game.start()