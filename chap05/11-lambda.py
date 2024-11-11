def print_price(price, func):
    print('価格は', func(price))


kakaku = 1000
print_price(kakaku, lambda price: price*2)
print_price(kakaku, lambda price: price)
print_price(kakaku, lambda price: int(price*1.1))

#print_price(kakaku, function(price) {
#    return int(price * 1.1);
#});

#print_price(kakaku, (price) => int(price * 1.1));

