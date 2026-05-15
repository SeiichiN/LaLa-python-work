# 練習 4.1.1
# warikan.py

import math

price = int(input('料金 > '))
ninzu = int(input('人数 > '))
peyment = math.ceil(price / ninzu)
# print(peyment)

print("料金:{:,}円、人数:{:2d}人、ひとり:{:,}円"
      .format(price, ninzu, peyment))
