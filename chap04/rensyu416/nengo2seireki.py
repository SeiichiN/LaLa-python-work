from nengos import nengos

nengo = input('年号を入力 > ')
nen = int(input('年 > '))
seireki = 0
for k, v in nengos.items():
    if k == nengo:
        seireki = v + nen - 1
print(f'西暦{seireki}年')