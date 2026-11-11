# 5.1.2

# リストそれ自体を変更
def plus_one(lst):
    for i in range(len(lst)):
        lst[i] += 1

# 新しいリストを作成
def _plus_one(lst):
    lst2 = []
    for n in lst:
        n += 1
        lst2.append(n)
    return lst2
    

a = [1,2,3]
plus_one(a)
print(a)
# [2, 3, 4]

