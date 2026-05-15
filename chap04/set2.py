# 4.6.2 集合演算

mammals = {'cat', 'dog', 'bear', 'bat', 'momonga'}
flies = {'sparrow', 'crow', 'pigeon', 'bat'}

# 積集合
flying_mammals = mammals & flies
print(flying_mammals)

# 積集合の反対
symmetric_diff = mammals ^ flies
print(symmetric_diff)

# 差集合（左-右）
non_flying_mammals = mammals - flies
print(non_flying_mammals)

# 和集合（両方）
union_animals = mammals | flies
print(union_animals)
