# プレイヤークラス

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.y = random.randint(0,4)
        self.x = random.randint(0,4)
    def move(self):
        print(f'{self.name}は動きます')

p1 = Player('太郎')
print('{}[{},{}]'.format(p1.name, p1.y, p1.x))
p1.move()

p2 = Player('花子')
print('{}[{},{}]'.format(p2.name, p2.y, p2.x))
p2.move()


        
