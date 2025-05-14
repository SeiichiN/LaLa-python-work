# p.119
# continue

total = 0
for i in range(100):  # 0..99
    if i % 3 == 0:
        continue  # 次の回
    print(i)
    total += i
print('合計は', total)
