# total2.py
# キーワードつきで引数を記述

def add_item(**kwprices):
    print(kwprices) # 辞書
    for item, price in kwprices.items():
        print(f'品目:{item} 値段:{price}円')
    
add_item(choco=200, cake=300,
         banana=250, sarad=100)

