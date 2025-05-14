# リスト内包表記

# range(1, 11) をもとにリストを作成する
# だたし、2のn乗のリストとする
# 1 .. 2 ** 1
# 2 .. 2 ** 2
# 3 .. 2 ** 3

lst = []
for n in range(1, 11):
    lst.append(2**n)
print(lst)

lst = [2**n for n in range(1, 11)]
print(lst)

## 偶数だけのリストをつくる
lst = []
for n in range(1,11):
    if n%2==0:
        lst.append(n)
print(lst)

lst = [n for n in range(1, 11) if n%2==0]
print(lst)
