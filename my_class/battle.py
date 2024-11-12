#
# Player と Monster のたたかい
#
import random
from character import Monster, Player

def battle (player, monster):
    while player.hp > 0 and monster.hp > 0:
        attack_p = random.randint(0, 20)
        monster.hp = monster.hp - attack_p
        print(f'{player.name}から {monster.type}への攻撃')
        if monster.hp > 0:
            print(f'{attack_p}のダメージを与えた。')
        else:
            print(f'{monster.type}を倒した。')
        attack_m = random.randint(0, 20)
        player.hp = player.hp - attack_m
        print(f'{monster.type}から {player.name}への攻撃')
        if player.hp > 0:
            print(f'{attack_m}のダメージを受けた。')
        else:
            print(f'{player.name}は倒れた。')
