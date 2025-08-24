class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


class Game:
    def __init__(self):
        # Create two players directly inside Game
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")
        self.current_player = self.player1
        self.board = [" "] * 9

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def player_move(self):
        while True:
            try:
                position = int(input(f"{self.current_player.name} ({self.current_player.mark}), choose a position (1-9): ")) - 1
                if position in range(9) and self.board[position] == " ":
                    self.board[position] = self.current_player.mark
                    break
                else:
                    print("Invalid position or already taken. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

    def check_win(self):
        b = self.board
        m = self.current_player.mark
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_combinations:
            if b[combo[0]] == b[combo[1]] == b[combo[2]] == m:
                return True
        return False

    def check_tie(self):
        return " " not in self.board

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.display_board()
        while True:
            self.player_move()
            self.display_board()
            if self.check_win():
                print(f"Congratulations {self.current_player.name}, you win!")
                break
            if self.check_tie():
                print("It's a tie!")
                break
            self.switch_player()

    @staticmethod
    def start():
        game = Game()
        game.play()

Game.start()
