# 4.3.6 リスト内包表記

# 基本形
# [n for n in リスト]

lst1 = [1,2,3,4,5]
lst2 = [n**2 for n in lst1]
print(lst2)

lst3 = [n*2 for n in range(1, 6)]
print(lst3)
# [2, 4, 6, 8, 10]

lst4 = [n*2 for n in range(1, 6) if n%2==0]
print(lst4)
# [4, 8]
