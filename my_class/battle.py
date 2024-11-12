#
# Player と Monster のたたかい
#
import random
from character import Monster, Player
from common import board

def next(player, monster):
    if player.hp <= 0 or monster.hp <= 0:
        return
    key = input(f'プレイヤー:{player.hp} モンスター:{monster.hp} > ')
    

def battle (player, monster):
    while player.hp > 0 and monster.hp > 0:
        player.attack(monster)
        next(player, monster)
        monster.attack(player)
        next(player, monster)
    if monster.hp <= 0:
        board[monster.y][monster.x] = '.'
        
