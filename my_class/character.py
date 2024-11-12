from common import board, get_blank_place, XSIZE, YSIZE
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.y, self.x = get_blank_place()
        self.hp = 100
    def location(self):
        print(f'[{self.y},{self.x}]')
    def take(self):
        item = board[self.y][self.x]
        if isinstance(item, Item):
            self.inventory.append(item)
            board[self.y][self.x] = '.'
    def move(self, dir):
        now = self.y, self.x
        if dir == 'w':
            self.x -= 1
            if self.x < 0:
                self.x = 0
        elif dir == 'e':
            self.x += 1
            if self.x >= XSIZE:
                self.x = XSIZE - 1
        elif dir == 'n':
            self.y -= 1
            if self.y < 0:
                self.y = 0
        elif dir == 's':
            self.y += 1
            if self.y >= YSIZE:
                self.y = YSIZE - 1
        if board[self.y][self.x] == '#':
            self.y, self.x = now
        self.location()
    def info_here(self):
        character = board[self.y][self.x]
        if character != '.':
            print(character.toString())
    def attack(self, monster):
        if self.hp <= 0:
            return
        print(f'{self.name}から {monster. type}への攻撃')
        attack_p = random.randint(0, 20)
        if attack_p == 0:
            print('攻撃失敗')
            return
        monster.hp = monster.hp - attack_p
        if monster.hp > 0:
            print(f'{attack_p}のダメージを与えた。')
        else:
            print(f'{monster.type}を倒した。')

class Character:
    def __init__(self, type):
        self.type = type
        self.y, self.x = get_blank_place()
        board[self.y][self.x] = self

class Monster(Character):
    def __init__(self, type):
        super().__init__(type)
        self.type = type
        self.hp = 100
    def toString(self):
        return self.type
    def attack(self, player):
        if self.hp <= 0:
            return
        print(f'{self.type}から {player.name}への攻撃')
        attack_m = random.randint(0, 20)
        if attack_m == 0:
            print("攻撃失敗")
            return
        player.hp = player.hp - attack_m
        if player.hp > 0:
            print(f'{attack_m}のダメージを受けた。')
        else:
            print(f'{player.name}は倒れた。')


class Item(Character):
    def __init__(self, type):
        super().__init__(type)
        self.type = type
        board[self.y][self.x] = self
    def toString(self):
        return self.type
