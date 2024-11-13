import random
from common import map, YSIZE, XSIZE

class Monster:
    def __init__(self, type):
        self.type = type
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
        map[self.y][self.x] = self
    def attack(self, player):
        if self.hp <= 0:
            return
        print(f'{self.type}は{player.name}を攻撃した！')
        attack_p = random.randint(0, self.max_attack_p)
        if attack_p == 0:
            print('攻撃失敗')
            return
        player.hp -= attack_p
        print(f'{player.name}に{attack_p}のダメージを与えた。')
        if player.hp <= 0:
            print(f'{self.type}は{player.name}を倒した！')


class Goblin(Monster):
    def __init__(self, type):
        self.hp = 70
        super().__init__(type)

class Dragon(Monster):
    def __init__(self, type):
        self.hp = 120
        super().__init__(type)
