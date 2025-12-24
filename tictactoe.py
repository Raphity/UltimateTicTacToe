"""TicTacToe class file"""
from os import system
from custom_exceptions import SquareNotEmptyError, SquareNotFoundError
from bot import bot


class TicTacToe:
    """TicTacToe class"""

    def __init__(self, board, turn, mode, difficulty) -> None:
        """Init function"""

        self.board = board
        self.turn = turn
        self.mode = mode
        self.difficulty = difficulty

    def place_symbole(self):
        """Method to place symbol to the board var"""

        raw = 1.1
        col = 1.1
        symbol = " "
        square_place = (0, 0)

        # Solo and bot turn
        if self.turn % 2 == 0 and "solo" == self.mode:
            symbol = "X"
            square_place = bot(self.board, self.turn, self.difficulty)
            raw = square_place[0]
            col = square_place[1]

        # Multiplayer
        elif "solo" != self.mode:

            if self.turn % 2 == 0:
                symbol = "X"
            else:
                symbol = "O"

            while not isinstance(raw, int) or \
                    not isinstance(col, int):
                try:
                    raw = int(input("Select raw (0-2): "))
                    col = int(input("Select column (0-2): "))
                except ValueError:
                    print("Please enter num bewtween 0 and 2")
                    continue

        # Solo and player turn
        else:
            symbol = "O"
            while not isinstance(raw, int) or \
                    not isinstance(col, int):
                try:
                    raw = int(input("Select raw (0-2): "))
                    col = int(input("Select column (0-2): "))
                except ValueError:
                    print("Please enter num bewtween 0 and 2")
                    continue

        square = f"Raw: {raw}, Col: {col}"

        if not 0 <= raw <= 2:
            current_error = SquareNotFoundError(square=square)
            raise current_error

        if not 0 <= col <= 2:
            current_error = SquareNotFoundError(square=square)
            raise current_error

        if self.board[raw][col] != " ":
            current_error = SquareNotEmptyError(square=square,
                                                content=self.board[raw][col])
            raise current_error

        self.board[raw][col] = symbol
        self.turn += 1

    def game_finished(self):
        """This method checks if the winning or draw conditions are met
           Input: self
           Returs: bool
        """
        state = False

        # Check for raw
        for raw in range(3):
            if self.board[raw][0] != " " and len(set(self.board[raw])) == 1:
                print(f"{self.board[raw][0]} won !")
                state = True

        # Check for column
        for col in range(3):
            if self.board[0][col] != " " and self.board[0][col] == \
                    self.board[1][col] == self.board[2][col]:
                print(f"{self.board[0][col]} won !")
                state = True

        # Check for vertical (top to bottom)
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] \
                == self.board[2][2]:
            print(f"{self.board[0][0]} won !")
            state = True

        # Check for vertical (bottom to top)
        if self.board[0][2] != " " and self.board[0][2] == self.board[1][1] \
                == self.board[2][0]:
            print(f"{self.board[0][2]} won !")
            state = True

        # Check if board is full
        if 10 == self.turn:
            print("Draw !!!")
            state = True
        return state

    def display_board(self):
        """Replace clear by cls if
        you use windows cmd"""

        system("clear")
        print("--------")
        for raw in self.board:
            line = " |".join(raw)
            print(line)
            print("--------")
