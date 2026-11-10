# 4.5.5.一覧の表示

prefs = {
    'Osaka': 8838,
    'Nara' : 1324,
    'Kyoto': 2578,
    'Hyogo': 5565,
    }

lst = sorted(prefs)
# print(lst)
# ['Hyogo', 'Kyoto', 'Nara', 'Osaka']
# lst -- キーだけのリスト

lst = sorted(prefs.values())
# print(lst)
# [1324, 2578, 5565, 8838]

lst = sorted(prefs.items())
# print(lst)
##[('Hyogo', 5565),
## ('Kyoto', 2578),
## ('Nara', 1324),
## ('Osaka', 8838)]   

lst = sorted(prefs.items(), key=lambda x:x[1])
# print(lst)
# [('Nara', 1324),
#  ('Kyoto', 2578),
#  ('Hyogo', 5565),
#  ('Osaka', 8838)]

lst = sorted(prefs.items(),
             key=lambda x:x[1],
             reverse=True)
print(lst)
# [('Osaka', 8838), ('Hyogo', 5565),
# ('Kyoto', 2578), ('Nara', 1324)]
