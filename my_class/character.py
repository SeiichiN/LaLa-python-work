from common import board, get_blank_place, XSIZE, YSIZE

class Character:
    def __init__(self, type):
        self.type = type
        self.y, self.x = get_blank_place()


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.y, self.x = get_blank_place()
        self.hp = 100
    def location(self):
        print(f'[{self.y},{self.x}]')
    def take(self):
        thing = board[self.y][self.x]
        if thing.type == 'gold' or thing.type == 'potion':
            self.inventory.append(thing)
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

class Monster(Character):
    def __init__(self, type):
        super().__init__(type)
        self.type = type
        self.hp = 100
        board[self.y][self.x] = self
    def toString(self):
        return self.type

class Item(Character):
    def __init__(self, type):
        super().__init__(type)
        self.type = type
        board[self.y][self.x] = self
    def toString(self):
        return self.type
