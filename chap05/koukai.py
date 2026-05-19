# 高階関数

def calc_price(price, func):
    return func(price)

def keigen_tax(price):
    return int(price + price * 0.08)

def normal_tax(price):
    return int(price + price * 0.1)

banana = 200
sake = 1200

banana_yen = calc_price(banana, keigen_tax)
print(f'banana:{banana_yen}円')

sake_yen = calc_price(sake, normal_tax)
print(f'sake: {sake_yen}円')
