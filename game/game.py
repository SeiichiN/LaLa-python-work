#
# 5x5の盤面をプレーヤーが移動する
#
from player import Player
import random
from common import YSIZE, XSIZE, map
from monster import Goblin

goblin = Goblin('ゴブリン')        
p1 = Player('Taro')
print(f'{p1.name} Y:{p1.y} X:{p1.x}')
while True:
    stm = input('wesn:移動 q:終了 > ').lower()
    if stm == 'q':
        break
    elif stm=='w' or stm=='e' or stm=='s' or stm=='n':
        p1.move(stm)
