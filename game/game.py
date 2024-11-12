#
# 5x5の盤面をプレーヤーが移動する
#

import random

YSIZE = 5
XSIZE = 5
map = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '.'],
    ['.', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '.']
    ]

# Playerクラス
#   インスタンス変数
#     name = 初期化時に設定
#     y = ランダム 0..4
#     x = ランダム 0..4
class Player:
    def __init__(self, name):
        self.name = name
        loc_ok = False
        while not loc_ok:
            self.y = random.randint(0,YSIZE-1)
            self.x = random.randint(0,XSIZE-1)
            if map[self.y][self.x] == '.':
                loc_ok = True
    def move(self, dir):
        if dir == 'w':  #←
            self.x -= 1
            if self.x < 0:
                self.x = 0
        elif dir == 'e':  #→
            self.x += 1
            if self.x >= XSIZE:
                self.x = XSIZE-1
        elif dir == 'n':  #↑
            self.y -= 1
            if self.y < 0:
                self.y = 0
        elif dir == 's':  #↓
            self.y += 1
            if self.y >= YSIZE:
                self.y = YSIZE-1
        self.location()
    def location(self):
        print(f'現在:[{self.y}:{self.x}]')
        

        
        
p1 = Player('Taro')
print(f'{p1.name} Y:{p1.y} X:{p1.x}')
while True:
    stm = input('wesn:移動 q:終了 > ').lower()
    if stm == 'q':
        break
    elif stm=='w' or stm=='e' or stm=='s' or stm=='n':
        p1.move(stm)
