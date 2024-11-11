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
        self.inventory = []
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
    stm = input('W:E:N:S H:help L:見る T:取る Q:終了 > ').lower()
    if stm == 'w':
        p1.x -= 1
        if p1.x < 0:
            p1.x = 0
    elif stm == 'e':
        p1.x += 1
        if p1.x >= XSIZE:
            p1.x = XSIZE-1
    elif stm == 'n':
        p1.y -= 1
        if p1.y < 0:
            p1.y = 0
    elif stm == 's':
        p1.y += 1
        if p1.y >= YSIZE:
            p1.y = YSIZE-1
    elif stm == 'l':
        print(board[p1.y][p1.x])
    elif stm == 'h':
        print('   N  ')
        print('   ↑ ')
        print('w← →E')
        print('   ↓ ')
        print('   S  ')
        continue
    elif stm == 't':
        thing = board[p1.y][p1.x]
        if thing == 'gold' or thing == 'potion':
            p1.inventory.append(thing)
            board[p1.y][p1.x] = '.'
    p1.location()
    print_info(p1.y, p1.x)
        
