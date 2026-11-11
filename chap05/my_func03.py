# 5.1.3 変数のスコープ

def calc(price):
    global tax
    tax = 0.05
    return price + int(price * tax)

tax = 0.1
zeikomi = calc(1000)
print('税込:', zeikomi)
print('tax:', tax)
