# アドベンチャーゲーム

import random

map = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'P', '.'],
    ['.', 'G', '.', '.', '.'],
    ['.', '.', 'S', 'E', '.'],
    ['.', '.', '.', '.', '.'],
    ]
# print(map[2][1])


def printMap(pos):
    for y in range(0, 5):
        for x in range(0, 5):
            if pos[0] == y and pos[1] == x:
                print('@', end='|')
            else:
                print(map[y][x], end='|')
        print()


def move(pos):
    y = pos[0]
    x = pos[1]
    moji = input('w↑ s↓ a← d→ q:終了 > ')
    if moji == 'w':
        y -= 1
        if y < 0:
            y = 0
    elif moji == 's':
        y += 1
        if y > 4:
            y = 4
    elif moji == 'a':
        x -= 1
        if x < 0:
            x = 0
    elif moji == 'd':
        x += 1
        if x > 4:
            x = 4
    elif moji == 'q':
        return 'q'
    #print(f'現在:[{y},{x}]')
    pos[0] = y
    pos[1] = x
    printMap(pos)


y = random.randint(0, 4)
x = random.randint(0, 4)
pos = [y, x]
#print(f'現在:[{y},{x}]')
printMap(pos)
while True:
    # 移動
    result = move(pos)
    if result == 'q':
        break
    if map[pos[0]][pos[1]] == 'G':
        print('ゴブリンが現れた！')
print('終了')
