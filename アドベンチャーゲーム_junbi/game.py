# アドベンチャーゲーム

import random
from player import Player
from monster import Monster

map = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'P', '.'],
    ['.', 'G', '.', '.', '.'],
    ['.', '.', 'S', 'E', '.'],
    ['.', '.', '.', '.', '.'],
    ]
# print(map[2][1])


def printMap(player):
    for y in range(0, 5):
        for x in range(0, 5):
            if player.y == y and player.x == x:
                print('@', end='|')
            else:
                print(map[y][x], end='|')
        print()




p1 = Player('太郎')
goblin = Monster('ゴブリン')
slime = Monster('スライム')
#print('{}[{},{}]'.format(p1.name, p1.y, p1.x))

printMap(p1)
while True:
    # 移動
    result = p1.move()
    printMap(p1)
    if result == 'q':
        break
    if map[p1.y][p1.x] == 'G':
        print('ゴブリンが現れた！')
        select = input('a:戦う r:逃げる > ')
        if select == 'a':
            p1.attack(goblin)
    if map[p1.y][p1.x] == 'S':
        print('スライムが現れた！')
        select = input('a:戦う r:逃げる > ')
        if select == 'a':
            p1.attack(slime)
        
print('終了')
