# 4.1.1 formatメソッド

import math

price = int(input('金額を入力 > '))
ninzu = int(input('人数を入力 > '))
peyment = price / ninzu
peyment = math.ceil(peyment)

formatTxt = "料金:{:,}円、人数:{:2d}人、ひとり:{:,}円"
msg = formatTxt.format(price, ninzu, peyment)
print(msg)

# print(f'料金:{price:,}円、人数:{ninzu:2d}人、ひとり:{peyment:,}円')
