# p.201
# 真偽値を戻り値とする関数

def is_positive(i):
    return i > 0


a = -10
if is_positive(a):
    print('aの値は正です')
else:
    print('aの値は負またはゼロです')
