# 4.6.2 集合演算

mammals = {'cat', 'dog', 'bear', 'bat', 'momonga'}
flies = {'sparrow', 'crow', 'pigeon', 'bat', 'momonga'}

# 積集合
flying_mammals = mammals & flies
# print(flying_mammals)
# {'bat', 'momonga'}

# 対称差（排他的論理和）（積集合の反対）
symmetric_diff = mammals ^ flies
# print(symmetric_diff)
# {'sparrow', 'bear', 'pigeon', 'crow', 'cat', 'dog'}

# 差集合
non_flying_mammals = mammals - flies
# print(non_flying_mammals)
# {'dog', 'cat', 'bear'}

# 和集合
union_animals = mammals | flies
print(union_animals)
# {'cat', 'bear', 'bat', 'crow',
#  'momonga', 'sparrow', 'dog', 'pigeon'}
