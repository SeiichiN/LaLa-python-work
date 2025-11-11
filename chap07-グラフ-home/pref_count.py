# p277
# 都道府県別来館者数

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

sorted = sorted(pref_count_dict.items(), key=lambda x:x[1], reverse=True)
with open('sorted.txt', 'w', encoding='UTF-8') as out_f:
    for line in sorted:
        out_f.write(line[0] + ',' + str(line[1]) + '\n')
    
