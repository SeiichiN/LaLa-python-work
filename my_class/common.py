import random

YSIZE = 5
XSIZE = 5
board = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.']
    ]

def get_blank_place():
    is_blank = False
    while not is_blank:
        x = random.randint(0, XSIZE-1)
        y = random.randint(0, YSIZE-1)
        if board[y][x] == '.':
            is_blank = True
    return y, x
