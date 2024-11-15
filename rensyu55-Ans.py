# 練習問題55本ノック・解答例

def pp(n):
    print(f'{n}:', end=' ')

# (1)
pp(1)
x = 2
print(x*3)

# (2)
pp(2)
a = 100
b = 200
a, b = b, a
print(a, b)


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

# 6
pp(6)
a=5
b=10
print(max(a, b))

# 7
pp(7)
a=5
print(a%2==0)

# 8
pp(8)
a = 'python'
print(a[2])

# 9
pp(9)
a='py'
b='thon'
print(a+b)

# 10
pp(10)
a=5
b=3
print(f'{a}%{b}={a%b}')

#11
pp(11)
a='some1'
print(a.replace('1', 'one'))

#12
pp(12)
a = 'This Is A Sentence .'
print(a.lower())

#13
pp(13)
print(a.upper())

#14
pp(14)
a = 'How many characters?'
print(len(a))

#15
pp(15)
a = '34'
b = '43'
print(int(a)+int(b))


# 16
pp(16)
a = [1,2,3,4,5]
print(a[3])

# 17
pp(17)
li1 = [1,2,3]
li2 = [4,5]
print(li1+li2)

#18
pp(18)
a = [1,2,3,4,5]
a.append(6)
a.append(7)
print(a)

#19
pp(19)
a.insert(1, 100)
print(a)

#20
pp(20)
a = [1,2,3,4,5]
b = [n for n in a if n%2==0]
print(b)


# 21
a = [1,2,3,4,5]
pp(21)
b = []
for n in a:
    i = a.index(n)
    if i%2==0:
        b.append(n)
print(b)

# 21
a = [1,2,3,4,5]
pp(21)
b = []
for n in range(0, 5):
    if n%2==0:
        b.append(a[n])
print(b)

#22
pp(22)
a = [11,22,33,44,55,66]
print(len(a))


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

#32
pp(32)
a = [1,2,3,4,5]
a.reverse()
print(a)

#33
pp(33)
a = [1,1,2,3,3,4,5]
print(set(a))

#34
pp(34)
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2)

#35
pp(35)
print(set1 | set2)

#36
pp(36)
print(set1 - set2)

#37
pp(37)
data1 = {'a':1, 'B':2}
data2 = 'hoge'
data3 = {1,2,3,4,5}
print(type(data1))
print(type(data2))
print(type(data3))

#38
pp(38)
a = 'This is sentence .\n'
print(a.strip())

#39
pp(39)
a = 'C C++ // python java'
b = a.split(' ')
print(b)
c = a.split('/')
print(c)

#40
pp(40)
a = ['This', 'is', 'a', 'sentence']
b = ' '.join(a)
print(b)

#41
pp(41)
a = [11,2,7,13,5]
print(max(a))

#42
pp(42)
print(min(a))

#43
pp(43)
print(sum(a))

#44
pp(44)
a = [5,3,1,4,2]
a.sort()
print(a)

#45
pp(45)
li = [
    {'a':6, 'b':7, 'c':6},
    {'a':4, 'b':2, 'c':3},
    {'a':1, 'b':5, 'c':8},
    ]
li2 = sorted(li, key=lambda x:x['b'], reverse=True)
print(li2)

#46
pp(46)
a = [n for n in range(0,100)]
print(a)

#47
pp(47)
a = [5,4,3,2,1]
b = [n + a.index(n) for n in a]
print(b)

#48
pp(48)
a = 0
b = 5
try:
    print(a/b)
    print(b/a)
except ZeroDivisionError:
    print('zero division')

#49
pp(49)
a = 10
b = 5
print(a|b, a&b, a^b)

#50
import math
sita = math.pi / 3
a = math.sin(sita)**2 + math.cos(sita)**2
print(a)

def ep(n):
    print(f'演習{n}:', end=' ')

#ex1
ep(1)
li_1 = list(range(1, 32))
li_2 = list(range(1, 13))
count = 0
for n1 in li_1:
    for n2 in li_2:
        count = count+1 if (n1%10)==(n2%10) else count+0
print(count)

#ex2
ep(2)
dic = {'two':324, 'four':830, 'three':493,
       'one':172, 'five':1024}
#a = sorted(dic.items())
a = sorted(dic.items(), key=lambda x:x[1])
b = [k for k, v in a]
print(b)

#ex3
ep(3)
nums = [1,2,4,3,2,1,5,1]
num2freq = {}
for n in range(min(nums), max(nums)+1):
    num2freq[n] = 0
for n in range(min(nums), max(nums)+1):
    for x in nums:
        if x == n:
            num2freq[n]+=1
print(num2freq)

#ex4
ep(4)
doc = 'i bought an apple .\ni ate it .\nit is delicious .'
listA = doc.split('\n')
listB = [n.split(' ') for n in listA]
#print(listB)
word2freq = {}
for b in listB:
    for a in b:
        if a in word2freq:
            word2freq[a] += 1
        else:
            word2freq[a] = 1
print(word2freq)

#ex5
ep(5)
list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]
set1 = set(list1)
set2 = set(list2)
jac = len(set1 & set2) / len(set1 | set2)
print(jac)



