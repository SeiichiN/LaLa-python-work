# 5.1.4 引数

def calc(price, tax):
    return int(price + price * tax)

print(calc(1000, 0.1))
print(calc(tax=0.1, price=1000))
