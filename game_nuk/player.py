
import random
from common import YSIZE, XSIZE, map
from character import Actor

# Playerクラス
#   インスタンス変数
#     name = 初期化時に設定
#     y = ランダム 0..4
#     x = ランダム 0..4
class Player(Actor):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 100
        self.max_attack_p = 20
        self.inventory = []
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
    def status(self):
        inventory_list = ''
        for item in self.inventory:
            inventory_list += item.type
        print(f'HP:{self.hp} 持ち物:{inventory_list}')
    def take(self):
        item = map[self.y][self.x]
        if item.type == 'potion' or item.type == 'ポーション':
            self.inventory.append(item)
            map[self.y][self.x] = '.'
            print(f'{self.name}は{item.type}を装備した')
        else:
            print(item.type)
    def use(self):
        for item in self.inventory:
            if item.type == 'potion' or item.type == 'ポーション':
               self.hp = item.hp
               print(f'{self.name}は{item.type}を飲んだ')
               print(f'HPが{self.hp}になった')
               self.inventory.remove(item)
            else:
                print(item.type)


