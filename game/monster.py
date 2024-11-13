import random
from common import map, YSIZE, XSIZE

class Monster:
    def __init__(self, type):
        self.type = type
        self.hp = 100
        self.set_location()
    def set_location(self):
        loc_ok = False
        while not loc_ok:
            self.y = random.randint(0,YSIZE-1)
            self.x = random.randint(0,XSIZE-1)
            if map[self.y][self.x] == '.':
                loc_ok = True
        map[self.y][self.x] = self    

class Goblin(Monster):
    def __init__(self, type):
        super().__init__(type)
        