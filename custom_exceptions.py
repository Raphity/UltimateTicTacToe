from time import sleep


class SquareNotEmptyError(Exception):
    def __init__(self, *args: object, square, content) -> None:
        super().__init__(*args)
        self.square = square
        self.content = content

    def show_error(self):
        print(f"Square: {self.square} is used by {self.content}")
        sleep(3)


class SquareNotFoundError(Exception):
    def __init__(self, *args: object, square) -> None:
        super().__init__(*args)
        self.square = square

    def show_error(self):
        print(f"Square: {self.square} is out of bounds")
        sleep(3)
