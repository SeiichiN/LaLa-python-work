# 4.1.2 リスト
# 気温データを入力

import statistics

# temp = []
# for hour in range(8, 18):
#     kion = float(input(f'{hour}時を入力してください > '))
#     temp.append(kion)

temp = [7.8, 9.1, 10.2, 11.0, 12.5, 12.4, 14.3, 13.8, 12.9, 12.4]

for i in range(len(temp)):
    print(f'{i+8:2d}時の気温: {temp[i]}度')

# 平均気温を求める
avg = statistics.mean(temp)  # 11.64
avg = round(avg, 1)
print(f'平均気温: {avg}度')

