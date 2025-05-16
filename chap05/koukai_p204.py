# p.204
# 高階関数

def print_price(price, func):
    print('価格は' + func(price))

def without_tax(price):
    return f'税抜き{price}円'

def with_tax(price):
    return f'税込み{price*1.1}円'

print_price(800, without_tax)
print_price(800, with_tax)
