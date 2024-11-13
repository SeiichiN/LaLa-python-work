import random
from character import Character

class Monster(Character):
    def __init__(self, mtype):
        super().__init__()
        self.type = mtype
        self.hp = 100
        self.max_attack_p = 20
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
    def __init__(self, mtype):
        self.hp = 70
        super().__init__(mtype)

class Dragon(Monster):
    def __init__(self, mtype):
        self.hp = 120
        super().__init__(mtype)
