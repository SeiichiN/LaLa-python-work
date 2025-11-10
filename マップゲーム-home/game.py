# マップを使ったゲーム

import random

map = [['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.']]

def look():
    print(f'[{py}:{px}]')
    print(map[py][px])
    

def get_position():
    while True:
        y = random.randrange(5)
        x = random.randrange(5)
        if map[y][x] == '.':
            break
    return (y, x)


def set_position(ch):
    y, x = get_position()
    map[y][x] = ch


def move(cmd):
    global py, px
    if cmd == 'w':
        py = max(py-1, 0)
    elif cmd == 's':
        py = min(py+1, 4)
    elif cmd == 'a':
        px = max(px-1, 0)
    elif cmd == 'd':
        px = min(px+1, 4)
    
    

# プレーヤーの位置
py, px = get_position()

# キャラクターの位置
set_position('p')
set_position('g')
set_position('s')

# プレーヤーの場所の位置情報
look()

while True:
    # wsadのどれかを入力
    cmd = input('w↑s↓a←d→ q:end > ')
    if cmd in ['w', 's', 'a', 'd']:
        move(cmd)
    elif cmd == 'q':
        break
    # 現在位置表示
    look()

print('Game End')    
