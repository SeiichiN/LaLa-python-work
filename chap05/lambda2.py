# 5.2 高階関数

def calc_price(price, func):
    return func(price)

banana = 200
sake = 1200

banana_yen = calc_price(banana, lambda x: [y=x*1.08, int(y)] )
print(f'banana:{banana_yen}円')

sake_yen = calc_price(sake, lambda x: int(x*1.1))
print(f'sake:{sake_yen}円')
