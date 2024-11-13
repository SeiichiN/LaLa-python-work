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
        self.max_attack_p = 20
        self.set_location()
    def set_location(self):
        loc_ok = False
        while not loc_ok:
            self.y = random.randint(0,YSIZE-1)
            self.x = random.randint(0,XSIZE-1)
            if map[self.y][self.x] == '.':
                loc_ok = True
    def move(self, dir):
        before_place = (self.y, self.x)
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
        print(f'{self.name}は{monster.type}を攻撃した！')
        attack_p = random.randint(0, self.max_attack_p)
        if attack_p == 0:
            print('攻撃失敗')
            return
        monster.hp -= attack_p
        print(f'{monster.type}に{attack_p}のダメージを与えた。')
        if monster.hp <= 0:
            print(f'{self.name}は{monster.type}を倒した！')
            map[self.y][self.x] = '.'
    def battle(self):
        monster = map[self.y][self.x]
        while self.hp > 0 and monster.hp > 0:
            self.attack(monster)
            monster.attack(self)
            if self.hp > 0 and monster.hp > 0:
                input(f'プレーヤー:{self.hp} {monster.type}:{monster.hp} > ')


