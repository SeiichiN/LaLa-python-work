import random
from common import YSIZE, XSIZE, map

# Playerクラス
#   インスタンス変数
#     name = 初期化時に設定
#     y = ランダム 0..4
#     x = ランダム 0..4
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.y = None
        self.x = None
        self.set_location()
    def set_location(self):
        loc_ok = False
        while not loc_ok:
            self.y = random.randint(0, YSIZE-1)
            self.x = random.randint(0, XSIZE-1)
            if map[self.y][self.x] == '.':
                loc_ok = True
    def move(self, direction):
        before_place = (self.y, self.x)
        if direction == 'w':  #←
            self.x -= 1
            if self.x < 0:
                self.x = 0
        elif direction == 'e':  #→
            self.x += 1
            if self.x >= XSIZE:
                self.x = XSIZE-1
        elif direction == 'n':  #↑
            self.y -= 1
            if self.y < 0:
                self.y = 0
        elif direction == 's':  #↓
            self.y += 1
            if self.y >= YSIZE:
                self.y = YSIZE-1
        if map[self.y][self.x] == '#':
            self.y, self.x = before_place
        self.location()
        self.look()
    def location(self):
        print(f'現在:[{self.y}:{self.x}]', end=' ')
    def look(self):
        sight = map[self.y][self.x]
        if sight == '.':
            print('何もありません')
        else:
            print(sight.type, 'がいた！')
    def attack(self, monster):
        if self.hp <= 0:
            return
        print(f'{self.name}は{monster.type}を攻撃した')
        ap = random.randint(0, 20)
        if ap == 0:
            print('攻撃は失敗した')
            return
        monster.hp -= ap
        print(f'{monster.type}のHPを{ap}減らした')
        if monster.hp <= 0:
            print(f'{monster.type}を倒した')
