# 4.1.2 リスト
# 気温データをタプルのリストで管理

import statistics

# temp = []
# for hour in range(8, 18):
#     kion = float(input(f'{hour}時を入力してください > '))
#     temp.append((hour, kion))

temp = [(8, 7.8), (9, 9.1),
        (10, 10.2), (11, 11.0),
        (12, 12.5), (13, 12.4),
        (14, 14.3), (15, 13.8),
        (16, 12.9), (17, 12.4)]

for h, t in temp:
    print(f'{h:2d}時の気温: {t}度')

# 平均気温を求める
t_lst = [t for h, t in temp]
avg = statistics.mean(t_lst)  # 11.64
avg = round(avg, 1)
print(f'平均気温: {avg}度')

