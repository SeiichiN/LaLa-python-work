def print_price(price, func):
    print('価格は', func(price))

def nibai(price):
    return price * 2

def price_without_tax(price):
    return price

def price_with_tax(price):
    return int(price*1.1)

kakaku = 1000
#print_price(kakaku, nibai)
print_price(kakaku, price_without_tax)
print_price(kakaku, price_with_tax)
