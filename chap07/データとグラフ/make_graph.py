# グラフにする

import matplotlib
import matplotlib.pyplot as plt

pref_count_dict = {}
with open('data/visitor_record.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        date, pref, num_adult, num_children = line.split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all
pref_count_sorted = sorted(pref_count_dict.items(), key=lambda x:x[1], reverse=True)

# グラフのデータをセット
labels = []
values = []
for l, v in pref_count_sorted:
    labels.append(l)  # 都道府県名
    values.append(v)  # 訪問者数
plt.rcParams['font.family'] = 'MyricaM M'
plt.xticks(rotation=300)
plt.bar(range(0, len(pref_count_sorted)), values, tick_label=labels)
plt.savefig('graph.png')

