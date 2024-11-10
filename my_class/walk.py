#
# 5x5の board(盤)上を Playerクラスのインスタンスが
# 移動するプログラム
#
import random

boad = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.']
    ]

class Player:
    def __init__(self):
        self.name = 'Taro'
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)
    def location(self):
        print(f'[{self.x},{self.y}]')
        
        
p1 = Player()
p1.location()

stm = ''
while stm != 'q':
    stm = input('移動:M 見る:L 終了:Q > ').lower()
    if stm == 'm':
        dir = input('左:W 右:E 上:N 下:S > ').lower()
        if dir == 'w':
            p1.x -= 1
        elif dir == 'e':
            p1.x += 1
        elif dir == 'n':
            p1.y -= 1
        elif dir == 's':
            p1.y += 1
        p1.location()
    if stm == 'l':
        print(boad[p1.y][p1.x])
        
