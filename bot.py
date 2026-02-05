from random import choice


def place_random(board):
    raw = 1
    col = 1
    while " " != board[raw][col]:
        options_raw = [0, 1, 2]
        options_col = [0, 1, 2]
        raw = choice(options_raw)
        col = choice(options_col)

    return (raw, col)


def cancel_line(board):
    """This function stops the human player
       from completing a line. Or it completes
       the line if it can
       input: board
       output: square position
    """
    selected_raw = 10
    selected_col = 10

    # check for diagonal
    if "O" == board[1][1]:
        if "O" == board[0][0] and " " == board[2][2]:
            selected_raw = 2
            selected_col = 2
        if "O" == board[2][2] and " " == board[0][0]:
            selected_raw = 0
            selected_col = 0
        if "O" == board[0][2] and " " == board[2][0]:
            selected_raw = 2
            selected_col = 0
        if "O" == board[2][0] and " " == board[0][2]:
            selected_raw = 0
            selected_col = 2

    # check for raws
    for raw in range(3):
        count_O_raw = 0
        count_X_raw = 0
        for col in range(3):
            if "O" == board[raw][col]:
                count_O_raw += 1
            if "X" == board[raw][col]:
                count_X_raw += 1
        if 2 == count_O_raw:
            for col in range(3):
                if " " == board[raw][col]:
                    selected_raw = raw
                    selected_col = col
        if 2 == count_X_raw:
            for col in range(3):
                if " " == board[raw][col]:
                    return (raw, col)

    # check for column
    for col in range(3):
        count_O_col = 0
        count_X_col = 0
        for raw in range(3):
            if "O" == board[raw][col]:
                count_O_col += 1
            if "X" == board[raw][col]:
                count_X_col += 1
        if 2 == count_O_col:
            for raw in range(3):
                if " " == board[raw][col]:
                    selected_raw = raw
                    selected_col = col
        if 2 == count_X_col:
            for raw in range(3):
                if " " == board[raw][col]:
                    return (raw, col)

    if 10 == selected_raw and 10 == selected_col:
        selected_raw, selected_col = place_random(board)

    return (selected_raw, selected_col)


def bot(board, turn, difficulty):
    valid = " "
    raw = 1
    col = 1

    if "easy" == difficulty:
        raw, col = place_random(board)
    else:
        if 2 == turn and valid == board[raw][col]:
            raw = 1
            col = 1
        elif 2 == turn:
            while valid != board[raw][col]:
                options_raw = [0, 2]
                options_col = [0, 2]
                raw = choice(options_raw)
                col = choice(options_col)
        else:
            raw, col = cancel_line(board)

    return (raw, col)
