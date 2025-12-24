"""Main file statrs the entire program"""
from custom_exceptions import SquareNotEmptyError, SquareNotFoundError
from tictactoe import TicTacToe


def main():
    """Menu function"""

    go_on = True
    while go_on:
        modes = "Solo\nMultiplayer"
        mode = str(input(f"Select mode:\n{modes}\nchoice: "))
        valid_modes = ["solo", "multiplayer"]

        while mode.lower() not in valid_modes:
            mode = str(input(f"Select mode:\n{modes}\nchoice: "))

        difficulty = None

        if "solo" == mode:
            valid_diff = ["easy", "hard"]
            difficulty = str(input("Difficulty\neasy\nhard\nChoice: "))

            while difficulty.lower() not in valid_diff:
                difficulty = str(input("Difficulty\neasy\nhard\nChoice: "))

        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        tictactoe = TicTacToe(board, turn=1, mode=mode, difficulty=difficulty)
        tictactoe.display_board()

        while not tictactoe.game_finished():
            try:
                tictactoe.place_symbole()
            except SquareNotFoundError as e:
                e.show_error()
                tictactoe.display_board()
                continue
            except SquareNotEmptyError as e:
                e.show_error()
                tictactoe.display_board()
                continue
            tictactoe.display_board()
        print("Game finished")

        choices = "continue \nstop"
        choice_str = str(input(f"Enter choice:\n{choices}\nChoice: "))
        valid_choices = ["stop", "continue"]

        while choice_str.lower() not in valid_choices:
            print("Enter valid choice!")
            choice_str = str(input(f"Enter choice:\n{choices}: "))

        if choice_str.lower() == "stop":
            go_on = False


if __name__ == "__main__":
    main()
