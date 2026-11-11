# 5.1.7 可変長引数

def total(*prices):
    sum = 0
    for price in prices:
        sum += price
    return sum

sum = total(800, 1000, 1200, 1800)
print(sum)
