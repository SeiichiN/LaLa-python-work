# data/sorted.txtを読み込む

import matplotlib
import matplotlib.pyplot as plt

labels = []
values = []
with open('data/sorted.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        l, v = line.rstrip('\n').split(',')
        labels.append(l)
        values.append(int(v))
plt.rcParams['font.family'] = 'MyricaM M'
plt.xticks(rotation=60)
plt.bar(range(len(values)), values, tick_label=labels)
plt.show()
plt.savefig('graph.png')
    
