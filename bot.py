from random import choice


def place_random(board):
    row = 1
    col = 1
    while " " != board[row][col]:
        options_row = [0, 1, 2]
        options_col = [0, 1, 2]
        row = choice(options_row)
        col = choice(options_col)

    return (row, col)


def cancel_line(board):
    """This function stops the human player
    from completing a line. Or it completes
    the line if it can
    input: board
    output: square position
    """
    selected_row = 10
    selected_col = 10

    # check for diagonal
    if "O" == board[1][1]:
        if "O" == board[0][0] and " " == board[2][2]:
            selected_row = 2
            selected_col = 2
        if "O" == board[2][2] and " " == board[0][0]:
            selected_row = 0
            selected_col = 0
        if "O" == board[0][2] and " " == board[2][0]:
            selected_row = 2
            selected_col = 0
        if "O" == board[2][0] and " " == board[0][2]:
            selected_row = 0
            selected_col = 2

    # check for rows
    for row in range(3):
        count_O_row = 0
        count_X_row = 0
        for col in range(3):
            if "O" == board[row][col]:
                count_O_row += 1
            if "X" == board[row][col]:
                count_X_row += 1
        if 2 == count_O_row:
            for col in range(3):
                if " " == board[row][col]:
                    selected_row = row
                    selected_col = col
        if 2 == count_X_row:
            for col in range(3):
                if " " == board[row][col]:
                    return (row, col)

    # check for column
    for col in range(3):
        count_O_col = 0
        count_X_col = 0
        for row in range(3):
            if "O" == board[row][col]:
                count_O_col += 1
            if "X" == board[row][col]:
                count_X_col += 1
        if 2 == count_O_col:
            for row in range(3):
                if " " == board[row][col]:
                    selected_row = row
                    selected_col = col
        if 2 == count_X_col:
            for row in range(3):
                if " " == board[row][col]:
                    return (row, col)

    if 10 == selected_row and 10 == selected_col:
        selected_row, selected_col = place_random(board)

    return (selected_row, selected_col)


def bot(board, turn, difficulty):
    valid = " "
    row = 1
    col = 1

    if "easy" == difficulty:
        row, col = place_random(board)
    else:
        if 2 == turn and valid == board[row][col]:
            row = 1
            col = 1
        elif 2 == turn:
            while valid != board[row][col]:
                options_row = [0, 2]
                options_col = [0, 2]
                row = choice(options_row)
                col = choice(options_col)
        else:
            row, col = cancel_line(board)

    return (row, col)
