# ゲーム
# 5x5のマス目の中を移動するゲーム
#
#
#   0 1 2 3 4
# 0|.|.|g|.|.|
# 1|.|.|.|.|.|
# 2|.|@|.|.|.|
# 3|.|.|.|p|.|
# 4|.|s|.|.|.|
#
# @: プレーヤー hp:100
# g: ゴブリン   ap: 30
# s: スライム   ap: 30
# p: ポーション hp: 100まで補充
# .: 何もない場所
#
# 移動:     w↑
#       ←a s↓d→  
#

import random
import sys

map = [ ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'] ]

YSIZE = 5
XSIZE = 5

def get_position():
    while True:
        y = random.randrange(YSIZE)
        x = random.randrange(XSIZE)
        if map[y][x] == '.':
            break
    return (y, x)


def set_item(item):
    y, x = get_position()
    map[y][x] = item


def print_help():
    print('移動: w:↑ s:↓ a:← d:→')
    print('q:終了')


def print_map():
    for y in range(YSIZE):
        print('|', end='')
        for x in range(XSIZE):
            if (y, x) == (py, px):
                print('@', end='|')
            else:
                print(map[y][x], end='|')
        print()


def look():
    place = map[py][px]
    if place == '.':
        print('何もありません')
    elif place == 'g':
        print('ゴブリンがいた！')
    elif place == 's':
        print('スライムがいた！')
    elif place == 'p':
        print('ポーションがあった！')
    
    
def cmd():
    global py, px
    cmd = input('command (h:help)> ')
    if cmd == 'w':
        py -= 1
        py = max(py, 0)
    elif cmd == 's':
        py += 1
        py = min(py, YSIZE-1)
    elif cmd == 'a':
        px -= 1
        px = max(px, 0)
    elif cmd == 'd':
        px += 1
        px = min(px, XSIZE-1)
    elif cmd == 'h':
        print_help()
    elif cmd == 'q':
        print('終了します')
        sys.exit()


# プレーヤーの初期位置
py, px = get_position()

# アイテム(モンスター)の初期位置
set_item('g')
set_item('s')
set_item('p')


while True:
    print_map()
    print(f'[{py}:{px}]')
    look()
    cmd()
