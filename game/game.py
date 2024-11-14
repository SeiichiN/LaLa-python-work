#
# 5x5の盤面をプレーヤーが移動する
#
from player import Player
from monster import Goblin, Dragon
from common import map
from item import Potion

def battle(player, monster):
    while player.hp > 0 and monster.hp > 0:
        print()
        player.attack(monster)
        if monster.hp <= 0:
            map[monster.y][monster.x] = '.'
        monster.attack(player)
        if player.hp <= 0:
            print('GAMEOVER')
            break
        input(f'{player.name}:{player.hp} {monster.type}:{monster.hp} > ')

goblin = Goblin('ゴブリン')
goblin.location()   # ゴブリン [2,3]
dragon = Dragon('ドラゴン')
dragon.location()   # ドラゴン [3,4]
potion = Potion('ポーション')
potion.location()
p1 = Player('Taro')
print(f'{p1.name} Y:{p1.y} X:{p1.x}')
while True:
    stm = input('wesn:移動 b:戦う q:終了 > ').lower()
    if stm == 'q':
        break
    elif stm=='w' or stm=='e' or stm=='s' or stm=='n':
        p1.move(stm)
    elif stm == 'b':
        battle(p1, map[p1.y][p1.x])

