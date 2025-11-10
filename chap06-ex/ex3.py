# 問題3

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


rec0 = Rectangle(5, 8)
rec1 = Rectangle(4, 6)

print('rec0の面積', rec0.get_area())
print('rec1の面積', rec1.get_area())
