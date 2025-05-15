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

y = random.randint(0, 4)
x = random.randint(0, 4)
pos = [y, x]
print(f'現在:[{y},{x}]')
moji = input('w↑ s↓ a← d→ > ')
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
print(f'現在:[{y},{x}]')

