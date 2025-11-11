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

            
