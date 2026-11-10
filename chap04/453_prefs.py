# 4.5.3 空の辞書

prefs = {}
prefs['Osaka'] = 8838
prefs['Nara'] = 1324
prefs['Kyoto'] = 2578
prefs['Hyogo'] = 5565
print(prefs)
# {'Osaka': 8838, 'Nara': 1324,
#  'Kyoto': 2578, 'Hyogo': 5565}

# 要素の取得(1)
print(f'兵庫県の人口は{prefs['Hyogo']}千人です')
# 兵庫県の人口は5565千人です

print('修正します')
prefs['Hyogo'] = 5465
# 要素の取得(2)
print(f'兵庫県の人口は{prefs.get('Hyogo')}千人です')
# 兵庫県の人口は5465千人です

del prefs['Kyoto']
print(prefs)
# {'Osaka': 8838, 'Nara': 1324, 'Hyogo': 5465}

