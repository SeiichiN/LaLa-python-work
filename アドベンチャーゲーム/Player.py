# プレイヤークラス

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.y = random.randint(0,4)
        self.x = random.randint(0,4)
    def move(self):
        moji = input('w↑ s↓ a← d→ q:終了 > ')
        if moji == 'w':
            self.y -= 1
            if self.y < 0:
                self.y = 0
        elif moji == 's':
            self.y += 1
            if self.y > 4:
                self.y = 4
        elif moji == 'a':
            self.x -= 1
            if self.x < 0:
                self.x = 0
        elif moji == 'd':
            self.x += 1
            if self.x > 4:
                self.x = 4
        elif moji == 'q':
            return 'q'
        return '_'

if __name__ == '__main__':
    p1 = Player('太郎')
    print('{}[{},{}]'.format(p1.name, p1.y, p1.x))
    p1.move()

    p2 = Player('花子')
    print('{}[{},{}]'.format(p2.name, p2.y, p2.x))
    p2.move()


        
