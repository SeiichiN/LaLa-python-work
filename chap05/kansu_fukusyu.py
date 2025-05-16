# 関数の復習

def add10():
    a = 0
    a += 10
    print(a) # 10

a = 10
add10()
print(a) # 10


def add20(b):
    b += 20
    print(b) #30

b = 10
add20(b)
print(b)  #10


def add30(c):
    c += 30
    print(c)
    return c

c = 10
d = add30(c)
print(d)


