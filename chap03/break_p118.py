# p.118
# break

total = 0
for i in range(10): # 0..9
    total += i
    if total > 20:
        break  # forを抜け出す
print(i, total)  # 6 21

