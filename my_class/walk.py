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
        print(f'[{self.x},{self.y}]')


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
    stm = input('移動:M 見る:L 終了:Q > ').lower()
    if stm == 'm':
        dir = input('左:W 右:E 上:N 下:S > ').lower()
        if dir == 'w':
            p1.x -= 1
            if p1.x < 0:
                p1.x = 0
        elif dir == 'e':
            p1.x += 1
            if p1.x >= XSIZE:
                p1.x = XSIZE
        elif dir == 'n':
            p1.y -= 1
            if p1.y < 0:
                p1.y = 0
        elif dir == 's':
            p1.y += 1
            if p1.y >= YSIZE:
                p1.y = YSIZE
        p1.location()
        print_info(p1.y, p1.x)
    if stm == 'l':
        print(board[p1.y][p1.x])
        
