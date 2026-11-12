# 5.1.5 関数の引数

def summary_scores(kokugo, sugaku, eigo, *others):
    #print(others)
    #print('sugaku:', sugaku)
    #print('eigo:', eigo)
    #print('kokugo:', kokugo)
    return [20, 10, 15]

summary_scores(eigo=80, kokugo=20, sugaku=70)

