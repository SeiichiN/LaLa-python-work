# 練習 5.1.2

import math

def calc_circle_area(radius):
    area = radius ** 2 * math.pi
    return round(area, 1)


hankei = 12.2
area = calc_circle_area(hankei)
print(f'円の面積は {area}')
