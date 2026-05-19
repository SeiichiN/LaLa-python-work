# temp_graph.py

import matplotlib
import matplotlib.pyplot as plt

# グラフのデータの入れ物
labels = []
temp_v = []

with open('temp.csv', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip('\n')
        month, temp = line.split(',')
        if month.startswith('2025') or month.startswith('月'):
            continue
        print(f'{month} 平均気温:{temp}')
        labels.append(month)
        temp_v.append(float(temp))

print(labels)
print(temp_v)
    
