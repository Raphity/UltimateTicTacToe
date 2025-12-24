"""Custom Exception file"""
from time import sleep


class SquareNotEmptyError(Exception):
    """Exception for square being uses"""

    def __init__(self, *args: object, square, content) -> None:
        """Init method"""

        super().__init__(*args)
        self.square = square
        self.content = content

    def show_error(self):
        """show error"""
        print(f"Square: {self.square} is used by {self.content}")
        sleep(3)


class SquareNotFoundError(Exception):
    """Exception for square being out of bounds"""

    def __init__(self, *args: object, square) -> None:
        """Init method"""

        super().__init__(*args)
        self.square = square

    def show_error(self):
        """show error"""

        print(f"Square: {self.square} is out of bounds")
        sleep(3)
