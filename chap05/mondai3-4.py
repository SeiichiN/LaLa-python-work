# 問題3-4

def get_absolute_value(value):
    if value < 0:
        return value * -1
    return value
    
v = float(input('数値 > '))
abs = get_absolute_value(v)
print(f'{v}の絶対値は{abs}')
