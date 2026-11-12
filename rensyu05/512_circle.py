# 5.1.2 円の面積

import math

def calc_circle_area(hankei):
    area = (hankei**2)*math.pi
    return area

area = calc_circle_area(10)
print(f'半径10の円の面積は{area}')
