# 4.3.5 for..inによる反復処理

lst1 = [1,2,3,4,5]
lst2 = []

for n in lst1:
    if n%2 == 0:
        lst2.append(n*2)

print(lst2)
