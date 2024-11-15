from common import YSIZE, XSIZE, map
import random


class Actor:
    def __init__(self):
        self.x = None
        self.y = None
        self.set_location()
    def set_location(self):
        loc_ok = False
        while not loc_ok:
            self.y = random.randint(0, YSIZE - 1)
            self.x = random.randint(0, XSIZE - 1)
            if map[self.y][self.x] == '.':
                loc_ok = True
    def get_location(self):
        return self.y, self.x


class Character(Actor):
    def __init__(self):
        super().__init__()
        map[self.y][self.x] = self

