total = 0
for i in range(100):  # 0..99
    if i % 3 == 0:
        continue
    total += i
    print(i, total)


print('合計は', total)
