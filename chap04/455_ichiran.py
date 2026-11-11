# 4.5.5.一覧の表示

prefs = {
    'Osaka': 8838,
    'Nara' : 1324,
    'Kyoto': 2578,
    'Hyogo': 5565,
    }
# print(prefs)

# keyが表示される
print('指定なし')
for n in prefs:
   print(n)
print('---------------')

# keys() -- keyが表示される
print('keys()')
for n in prefs.keys():
   print(n)
print('---------------')

print('values()')
# values() -- value が表示される
for n in prefs.values():
    print(n)
print('---------------')

print('items()')
# items() -- タプルが表示
for n in prefs.items():
    print(n)
##('Osaka', 8838)
##('Nara', 1324)
##('Kyoto', 2578)
##('Hyogo', 5565)
print('---------------')


print('items(), アンパック代入')
for k, v in prefs.items():
    print(k, v)
# Osaka 8838
# Nara 1324
# Kyoto 2578
# Hyogo 5565
print('---------------')
    
