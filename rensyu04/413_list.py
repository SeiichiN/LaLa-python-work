# 4.1.3 リスト内包表記

lst = [n*n for n in range(1, 11)]
print(lst)


lst1 = range(1, 11)
lst2 = [n*n for n in lst1]

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(lst[:4])  # [1, 4,, 9, 16]
print(lst[2:5]) # [9, 16, 25]
print(lst[3:])  # [16, 35, ....]

