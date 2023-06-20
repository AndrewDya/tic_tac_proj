class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.symbol = ""

    def occupy(self, symbol):
        if not self.is_occupied:
            self.is_occupied = True
            self.symbol = symbol


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        print(13 * '-')
        for i in range(0, 9, 3):
            row = self.cells[i:i + 3]
            print("|", end="")
            for cell in row:
                if cell.is_occupied:
                    print(f" {cell.symbol} |", end="")
                else:
                    print("   |", end="")
            print(f"\n{13 * '-'}")


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        while True:
            cell_number = input(f"{self.name},"
                                f" choose a cell number to make a move: ")
            if cell_number.isdigit() and 1 <= int(cell_number) <= 9:
                return int(cell_number)
            else:
                print("Invalid cell number."
                      " Please choose a number between 1 and 9.")


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1"), Player("Player 2")]

    def start_game(self):
        self.board.display()
        current_player_index = 0

        while True:
            current_player = self.players[current_player_index]
            cell_number = current_player.make_move()
            cell = self.board.cells[cell_number - 1]

            if cell.is_occupied:
                print("Cell occupied. Choose another.")
                continue

            symbol = "X" if current_player_index == 0 else "O"
            cell.occupy(symbol)
            self.board.display()

            if self.check_win(symbol):
                print(f"{current_player.name} wins!")
                current_player.wins += 1
                break

            if all(cell.is_occupied for cell in self.board.cells):
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 2

    def check_win(self, symbol):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # columns
            [1, 5, 9], [3, 5, 7]  # diagonals
        ]

        for combo in winning_combinations:
            if all(self.board.cells[num - 1].symbol == symbol for num in combo):
                return True

        return False

    def play_game(self):
        while True:
            self.start_game()
            self.print_score()
            if not self.play_again():
                break

    def print_score(self):
        print("Score:")
        for player in self.players:
            print(f"{player.name}: {player.wins}")
        print()

    def play_again(self):
        answer = input("Do you want to play again? (yes/no): ")
        if answer.lower() == "yes":
            self.board = Board()  # Очищаем поле перед началом новой игры
            return True
        return False


game = Game()
game.play_game()
