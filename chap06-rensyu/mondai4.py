# 問題4

class X:
    def __init__(self):
        print('[x]')
    def a(self):
        print('[x.a]')
    def b(self):
        print('[x.b]')


class Y(X):
    def __init__(self):
        super().__init__()
        print('[y]')
    def a(self):
        print('[y.a]')
        super().a()

    
x = X()   # (1) [x]
x.a()     # (2) [x.a]
x.b()     # (3) [x.b]
y = Y()   # (4) [x]
          #     [y]
y.a()     # (5) [y.a]
          #     [x.a]
y.b()     # (6) [x.b]