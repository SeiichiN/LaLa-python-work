# goblin.py

import random

from character import Character

class Goblin(Character):
    def attack(self, enemy):
        damage = random.randint(10, 21)
        enemy.hp -= damage
        print(f'{self.name}の斧による攻撃!')
        print(f'{enemy.name}に{damage}ポイントのダメージを与えた!')
        super().attack(enemy)


if __name__ == '__main__':
    goblin = Goblin('ゴブリン')
    
