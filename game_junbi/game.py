#
# 5x5の盤面をプレーヤーが移動する
#
from player import Player
from common import map
from monster import Goblin, Dragon
from item import Potion

def battle(player):
    monster = map[player.y][player.x]
    while player.hp > 0 and monster.hp > 0:
        print()
        player.attack(monster)
        monster.attack(player)
        if player.hp > 0 and monster.hp > 0:
            input(f'プレーヤー:{player.hp} {monster.type}:{monster.hp} > ')


goblin = Goblin('ゴブリン')
y, x = goblin.get_location()
print(f'goblin [{y},{x}]')

dragon = Dragon('ドラゴン')
y, x = dragon.get_location()
print(f'dragon [{y},{x}]')

potion = Potion('ポーション')
y, x = potion.get_location()
print(f'potion [{y},{x}]')
p1 = Player('Taro')
print(f'{p1.name} [{p1.y},{p1.x}]')
while True:
    stm = input('wesn:移動 b:戦う u:使う l:見る t:装備 q:終了 > ').lower()
    if stm == 'q':
        break
    elif stm=='w' or stm=='e' or stm=='s' or stm=='n':
        p1.move(stm)
    elif stm == 'b':
        battle(p1)
        if p1.hp <= 0:
            print('プレーヤーは倒れた。GAMEOVER')
            break
    elif stm == 'u':
        p1.use()
    elif stm == 't':
        p1.status()
    elif stm == 'l':
        p1.location()
        p1.look()


