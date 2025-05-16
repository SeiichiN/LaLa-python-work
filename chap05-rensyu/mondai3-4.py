# 第5章練習問題
# 問題3-4

def get_absolute_value(value):
    if value < 0:
        value *= -1
    return value

v = -3.3
v2 = get_absolute_value(v)
print(v2)
