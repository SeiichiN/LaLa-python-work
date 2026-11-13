import random

from character import Character

class Goblin(Character):
    def attack(self, enemy):
        damage = random.randint(10, 21)
        enemy.hp -= damage
        print(f'{self.name}の棍棒攻撃!')
        print(f'{enemy.name}に{damage}のダメージを与えた!') 
        super().attack(enemy)  # 親クラスのメソッド呼出


