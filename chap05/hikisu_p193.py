# p193
# 引数に渡されるのは値かアドレスか

def move(loc):
    loc[0] -= 1
    print('y:', loc[0])  # 2
    print('x:', loc[1])  # 1


pos = [3,1]
move(pos)
print(pos) # [2,1]


