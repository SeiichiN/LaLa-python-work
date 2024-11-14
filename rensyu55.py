
def pp(n):
    print(f'{n}:', end=' ')

# (1)
x = 2
pp(1)
print(x*3)

# (3)
a = 10
b = 2
pp(2)
print(a+b, a-b, a*b, a/b)

# (4)
a = 5
b = 3
pp(4)
print(a % b)

# 5
a = 5
b = 10
pp(5)
print(a**b)

# 16
pp(16)
a = [1,2,3,4,5]
print(a[3])

# 17
pp(17)
li1 = [1,2,3]
li2 = [4,5]
print(li1+li2)


# 21
a = [1,2,3,4,5]
pp(21)
for n in a:
    if n%2==0:
        print(n, end=' ')
        

# 22
a = [1,2,3,4,5]
pp(22)
for n in range(0, 5):
    if n%2==0:
        print(a[n], end=' ')

# 23
pp(23)
if 44 in [11,22,33,44,55]:
    print(True)
else:
    print(False)

    
# 24
pp(24)
a = [1,2,3,4,5]
print(a[0], a[-1])

#25
pp(25)
a = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
print(a)

#26
pp(26)
a = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
b = [n for n in a.keys()]
print(b)

#27
pp(27)
b = [n for n in a.values()]
print(b)

#28
pp(28)
b = [(k, v) for k, v in a.items()]
print(b)

#29
pp(29)
d = {'apple':10, 'grape':20, 'orange':30}
if not 'apple' in d.keys():
    d['apple'] = -1
if not 'pineapple' in d.keys():
    d['pineapple'] = -1
print(d)

#30
pp(30)
a = 'training'
print(a[1:5])

#31
pp(31)
a = 'understand'
b = [a[n] for n in range(len(a)) if n%2==1]
c = ''.join(b)
print(c)

    




