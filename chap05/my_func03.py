# my_func03.py

def calc(price):
    global tax
    tax = 0.05  # globalのtax を変更
    return price + int(price * tax)

tax = 0.1
zeikomi = calc(1000)
print('税込', zeikomi)  # 1050
print('tax:', tax)  # 0.05

