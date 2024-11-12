#
# 5x5の board(盤)上を Playerクラスのインスタンスが
# 移動するプログラム
#
import random
from common import board, get_blank_place, YSIZE, XSIZE
from character import Monster, Player, Item
from battle import battle

#def print_info(y, x):
#    if board[y][x] != '.':
#        print(board[y][x].toString())


goblin = Monster('goblin')
dragon = Monster('dragon')
gold = Item('gold')
potion = Item('potion')
p1 = Player('Taro')
p1.location()

stm = ''
while stm != 'q':
    stm = input('W:E:N:S H:help L:見る T:取る B:戦う Q:終了 > ').lower()
    if stm == 'w' or stm == 'e' or stm == 'n' or stm == 's':
        p1.move(stm)
    elif stm == 'l':
        print(board[p1.y][p1.x])
    elif stm == 'h':
        print('   N  ')
        print('   ↑ ')
        print('w← →E')
        print('   ↓ ')
        print('   S  ')
        continue
    elif stm == 't':
        p1.take()
    elif stm == 'B':
        monster = board[p1.y][p1.x]
        battle(p1, monster)
    # print_info(p1.y, p1.x)
        
