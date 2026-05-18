# calc.py
# 5.1.6 デフォルト引数

def calc(price, tax=0.1):
    return int(price + price * tax)

print(calc(1000))        #1100
print(calc(1000, 0.08))  #1080

