# p.204
# 高階関数

def print_price(price, func):
    print('価格は' + func(price))

print_price(
    800,
    lambda price: f'税抜き{price}円')
print_price(
    800,
    lambda price: f'税込み{price*1.1}円')
