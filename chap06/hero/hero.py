import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100

    def attack(self, enemy):
        damage = random.randrange(30)
        enemy.hp -= damage
        print(f'{self.name}の攻撃!')
        print(f'{enemy.name}に{damage}のダメージを与えた!')

    def run(self):
        print(f'{self.name}は逃げ出した!')
