import random
from common import map, YSIZE, XSIZE

class Monster:
    def __init__(self, m_type):
        self.type = m_type
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
        map[self.y][self.x] = self
    def location(self):
        print(f'{self.type} [{self.y}:{self.x}]')
    def attack(self, player):
        if self.hp <= 0:
            return
        print(f'{self.type}は{player.name}を攻撃した')
        ap = random.randint(0, 20)
        if ap == 0:
            print('攻撃は失敗した')
            return
        player.hp -= ap
        print(f'{player.name}のHPを{ap}減らした')
        if player.hp <= 0:
            print(f'{player.name}を倒した')


class Goblin(Monster):
    def __init__(self, g_type):
        super().__init__(g_type)

class Dragon(Monster):
    def __init__(self, d_type):
        super().__init__(d_type)
