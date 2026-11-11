# 5.1.8 キーと値で渡す

def add_item(**kwprices):
    print(kwprices)
    for item, price in kwprices.items():
        print(f'品目:{item}、値段:{price}')

add_item(choco=200,
         cake=300,
         banana=250,
         sarad=180)
##{'choco': 200, 'cake': 300, 'banana': 250, 'sarad': 180}
##品目:choco、値段:200
##品目:cake、値段:300
##品目:banana、値段:250
##品目:sarad、値段:180
