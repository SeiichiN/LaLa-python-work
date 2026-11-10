# 4.5.5.一覧の表示

prefs = {
    'Osaka': 8838,
    'Nara' : 1324,
#    'Kyoto': 2578,
    'Hyogo': 5565,
    }
print(prefs)

if 'Nara' in prefs:
   print(prefs['Nara'])
# 1324

if not 'Kyoto' in prefs.keys():
   prefs['Kyoto'] = 3578
print(prefs)

   
