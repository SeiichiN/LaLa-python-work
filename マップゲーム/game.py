# マップを使ったゲーム

import random

map = [['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.'],
       ['.', '.', '.', '.', '.']]

YSIZE = 5
XSIZE = 5

def get_position():
    y = random.randrange(YSIZE)
    x = random.randrange(XSIZE)
    return (y, x)


def set_position(ch):
    while True:
        y, x = get_position()
        if map[y][x] == '.':
            break
    map[y][x] = ch
    

def print_map():
    for y in range(YSIZE):
        print('|', end='')
        for x in range(XSIZE):
            if y == py and x == px:
                print('@', end='|')
            else:
                print(map[y][x], end='|')
        print()
    

def look():
    print_map()
    ch = map[py][px]
    if ch == 'p':
        print('ポーションがあった！')
    elif ch == 'g':
        print('ゴブリンがあらわれた！')
    elif ch == 's':
        print('スライムがあらわれた！')
    else:
        print('何もありません')


def move(cmd):
    global py, px
    if cmd == 'w':
        py = max(py-1, 0)
    elif cmd == 's':
        py = min(py+1, YSIZE-1)
    elif cmd == 'a':
        px = max(px-1, 0)
    elif cmd == 'd':
        px = min(px+1, XSIZE-1)


# プレーヤーの位置
py, px = get_position()

# キャラクターの配置
set_position('p')
set_position('g')
set_position('s')

# プレーヤーの場所の位置情報
look()

while True:
    cmd = input('w↑s↓a←d→ q:End > ')
    if cmd in ['w', 's', 'a', 'd']:
        move(cmd)
    elif cmd == 'q':
        break
    look()
print('終わります')   
