for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()


# 복사 해서 반복
words = ['cat','window','defenestrate']
for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

a = ['a','b','c','d']
for i in range(len(a)):
    print(i,a[i])

def f(a, L=None):
    L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

def ff(a, L=[]):
    L.append(a)
    return L

print(ff(1))
print(ff(2))
print(ff(3))

sep1 = '^'
print(sep1.join(['ss','343','11']))

def cheeseshop(kind, *argus, **keys):
    print("-- Do you have any", kind, "?")
    print("-- i'm sorry, we're all out of", kind)
    for arg in argus:
        print(arg)
    print("-"*40)
    for kw in keys:
        print(kw, ":", keys[kw])

cheeseshop("spicyburger","oh no", "hey", 
    shopkeeper="Michael Palin",client="John")

print(list(range(3, 6)))
args = [3,6]
print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts throuhgh it.", end=' ')
    print("E's", state, "!")

d2 = {
        "voltage":"four million",
        "state":"bleedin' demised",
        "action":"VOOOOM"
}

parrot(**d2)

def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4,'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

_str4 = 'Kim Lee Park Jung'
print(_str4.split(' '))

for s in list(_str4.split(' ')):
    print(s, end=" ")

print()

def prime(pNum):
    for x in range(2, pNum):
        for y in range(2, x):
            if(x % y == 0):
                print(x,'는', y, '*',x//y)
                break
        else:   
            print(x,'는 프라임 수')

prime(10)

# 리스트 컴프리헨션

vex = [-4, -2, 0 ,2 ,4]
print([x*2 for x in vex])
print([x for x in vex if x >= 0])
print([abs(x) for x in vex])
fruit = ['   banana  ', '   melon  ', '  apple  ']
print([weapon.strip() for weapon in fruit])
print([(x, x**2) for x in range(6)])

from math import pi
print([str(round(pi, i)) for i in range(1,6)])

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print([[y[x] for y in matrix] for x in range(4)])

transposed = []
for i in range(4):
    transposed.append([raw[i] for raw in matrix])

print(transposed)

print(list(zip(*matrix)))

for i, v in enumerate(['tic','tac','toc']):
    print(i, v)


questions = ['name', 'quest', 'favrite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print('What is your {0}? Iy is{1}.'.format(q,a))

for i in reversed(range(1,10,2)):
    print(i, end=' ')
print()
for i in range(9,0,-2):
    print(i, end=' ')
print()


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end=' ')
print()

import fibo
fibo.fibo(10)
print(fibo.fibo2(10))
print(fibo.__name__)

a, b, *c = (0,1,2,3,4,5)
print(a,b,c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*val, _, _ = scores
print(val)
_, *val, _ = scores
print(val)

inventory = {
    "메로나" : [300,20],
    "비비빅" : [400,3],
    "죠스바" : [250, 100]
}

print(str(inventory['메로나'][0]) + '원')

inventory['월드콘'] = [350,15]
print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

print(sum(list(icecream.values())))

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys,vals))
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

result2 = dict(zip(date, close_price))
print(result2)
