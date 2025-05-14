# 問題 3-2

total = 0
for num in range(10, 21):
    if num == 15:
        continue
    total += num
print('total=', total) # 150
