pref_count_dict = {}
with open('visitor_record.txt',
          'r',
          encoding='UTF-8') as f:
    for line in f:
        date, pref, num_a, num_c = line.split(',')
        num_all = int(num_a) + int(num_c)
        if pref in pref_count_dict:
            pref_count_dict[pref] += num_all
        else:
            pref_count_dict[pref] = num_all

pref_count_sorted = sorted(
    pref_count_dict.items(),
    key=lambda x:x[1],
    reverse=True)

for i in pref_count_sorted:
    print(i)
    
    
