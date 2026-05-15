# 辞書を並べ替える

prefs = {
    'Osaka': 8838,
    'Nara' : 1324,
    'Kyoto': 2578,
    'Hyogo': 5565
    }

lst_k = sorted(prefs)
# lst_k は、キーのみ

lst_v = sorted(prefs.values())
# lst_v は、バリューのみ

lst = sorted(prefs.items())
# lst は、キーとバリュー
# キーの昇順で並んでいる

lst2 = sorted(prefs.items(), key=lambda x:x[1])
# バリューの昇順

lst3 = sorted(prefs.items(),
              key=lambda x:x[1],
              reverse=True)
# バリューの降順
