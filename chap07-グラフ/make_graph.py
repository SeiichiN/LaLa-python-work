# p277
# 都道府県別来館者数

import matplotlib
import matplotlib.pyplot as plt

pref_count_dict = {}
path = 'data/visitor_record.txt'
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        date, pref, num_adult, num_children = line.split(',')
        num_all = int(num_adult) + int(num_children)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

pref_count_sorted = sorted(
    pref_count_dict.items(),
    key=lambda x:x[1],
    reverse=True)

## グラフィック描画
labels = []
values = []
for l, v in pref_count_sorted:
    labels.append(l)
    values.append(v)

# matplotlib.use('Agg')
plt.rcParams['font.family'] = 'MyricaM M'
plt.xticks(rotation=60)
plt.bar(range(len(pref_count_sorted)),
        values,
        tick_label=labels)
plt.savefig('graph.png')
plt.show()

    


