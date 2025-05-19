# アドベンチャーゲーム

import random
from player import Player

map = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'P', '.'],
    ['.', 'G', '.', '.', '.'],
    ['.', '.', 'S', 'E', '.'],
    ['.', '.', '.', '.', '.'],
    ]


def printMap(player):
    for y in range(0, 5):
        for x in range(0, 5):
            if player.y == y and player.x == x:
                print('@', end='|')
            else:
                print(map[y][x], end='|')
        print()


p1 = Player('太郎')
printMap(p1)

while True:
    # 移動
    result = p1.move()
    printMap(p1)
    if result == 'q':
        break
    if map[p1.y][p1.x] == 'G':
        print('ゴブリンが現れた！')
    elif map[p1.y][p1.x] == 'S':
        print('スライムが現れた！')
    elif map[p1.y][p1.x] == 'P':
        print('ポーション発見！')
    elif map[p1.y][p1.x] == 'E':
        print('エーテル発見！')
print('終了')

