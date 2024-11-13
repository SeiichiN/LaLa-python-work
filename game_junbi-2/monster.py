import random
from common import map, YSIZE, XSIZE

class Monster:
    def __init__(self, m_type):
        self.type = m_type
        self.hp = 100
        self.y = None
        self.x = None
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
    def __init__(self, m_type):
        super().__init__(m_type)
        