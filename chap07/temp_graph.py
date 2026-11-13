import matplotlib
import matplotlib.pyplot as plt

# 横軸と縦軸のリスト
labels = []  # 横軸（月）
temp_v = []  # 縦軸

with open('temp.csv', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip('\n')  # 空行をとる
        month, temp = line.split(',')
        if month.startswith('2025') or month.startswith('月'):
            continue
        labels.append(month)
        temp_v.append(float(temp))

# print(labels)
# print(temp_v)

plt.rcParams['font.family'] = 'MyricaM M'
plt.title('2025年の月平均気温の変化')
plt.plot(labels,
         temp_v,
         label='月平均気温の変化:2025年',
         color='#e15759')
plt.legend() # 凡例
plt.savefig('grahp.png')
plt.show()


