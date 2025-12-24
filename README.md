# TicTacToe Game

This is a command-line implementation of the TicTacToe game, where you can play either in **Solo** mode (against a bot) or **Multiplayer** mode (against another player).

### Features:
- **Solo Mode:** Play against a bot with different difficulty levels (Easy or Hard).
- **Multiplayer Mode:** Play with another person on the same device.
- **Error Handling:** Handles invalid moves like trying to place a symbol in an already occupied square or out-of-bounds move.
- **Game Display:** Displays the TicTacToe board after each turn.
- **Turn-based System:** Players take turns placing their symbols (`X` or `O`).

### Prerequisites:
- Python 3.x

### Setup:

1. **Clone the repository or download the files.**
   - Ensure you have all the Python files in the same directory:
     - `play.py`
     - `tictactoe.py`
     - `bot.py`
     - `custom_exceptions.py`

2. **Install necessary dependencies (if any).**
   - For this game, you don’t need any external libraries, just Python’s built-in libraries.

3. **Run the game.**
   - Open a terminal and navigate to the folder containing the files.
   - Run the following command:

     ```bash
     python play.py
     ```

4. **Play the game.**
   - You will be prompted to select a mode:
     - **Solo:** Play against the bot.
     - **Multiplayer:** Play with a friend.
   - In **Solo** mode, you can choose the difficulty (easy or hard).
   - Players will alternate turns to place their symbols on the 3x3 board.

### Warning:
- **Line 115 in `tictactoe.py` (the `display_board` method):** If you are using **Windows CMD** to run the game, replace `clear` with `cls` to clear the screen. The current code uses `clear` which is for Unix-based systems (Linux/macOS).
  
  To fix this:
  ```python
  system("cls")  # for Windows CMD

