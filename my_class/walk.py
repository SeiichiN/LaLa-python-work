#
# 5x5の board(盤)上を Playerクラスのインスタンスが
# 移動するプログラム
#
import random

YSIZE = 5
XSIZE = 5
board = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.']
    ]

class Player:
    def __init__(self, name):
        self.name = name
        self.x = random.randint(0, XSIZE-1)
        self.y = random.randint(0, YSIZE-1)
    def location(self):
        print(f'[{self.y},{self.x}]')


class Character:
    def __init__(self, type):
        self.type = type
        set_ok = False
        while not set_ok:
            self.x = random.randint(0, 4)
            self.y = random.randint(0, 4)
            if board[self.y][self.x] == '.':
                board[self.y][self.x] = self.type
                set_ok = True

def print_info(y, x):
    if board[y][x] != '.':
        print(board[y][x])

goblin = Character('goblin')
dragon = Character('dragon')
gold = Character('gold')
potion = Character('potion')
p1 = Player('Taro')
p1.location()

stm = ''
while stm != 'q':
    stm = input('M:移動 L:見る Q:終了 > ').lower()
    if stm == 'm':
        dir = input('W:左 E:右 N:上 S:下 > ').lower()
        if dir == 'w':
            p1.x -= 1
            if p1.x < 0:
                p1.x = 0
        elif dir == 'e':
            p1.x += 1
            if p1.x >= XSIZE:
                p1.x = XSIZE-1
        elif dir == 'n':
            p1.y -= 1
            if p1.y < 0:
                p1.y = 0
        elif dir == 's':
            p1.y += 1
            if p1.y >= YSIZE:
                p1.y = YSIZE-1
        p1.location()
        print_info(p1.y, p1.x)
    if stm == 'l':
        print(board[p1.y][p1.x])
        
