# answer = input('입력 : ')
# print(answer*2)

# out = int(input('num : '))

# if out % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

# out = int(input('입력 : '))
# out = out - 20

# if out < 0:
#     print(0)
# elif out >= 0 and out <= 255:
#     print(out)
# else:
#     print(255)

# out = input('입력 : ')

# # if out.split(':')[1] == '00':
# if out[:-2] == '00':
#     print('정각입니다.')
# else:
#     print('정각이 아닙니다.')

# fruit = ['사과', '포도', '홍시']

# # print(fruit.count('사2과'))

# if fruit.count(out) > 0:
#     print('정답')
# else:
#     print('오답')


# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

# if out in warn_investment_list:
#     print('투자 경고 종목')
# else:
#     print('투자 경고 목록이 아님')
# out = input('입력 : ')

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

# if out in list(fruit.keys()):
#     print('정답')
# else:
#     print('오답')

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# out = input('입력 : ')

# if out in list(fruit.values()):
#     print('정답')
# else:
#     print('오답')


# if out.isupper():
#     print(out.lower())
# else:
#     print(out.upper())

# out = input('입력 : ')

# transe = {
#     "달러"  : 1167,
#     "엔"    : 1.096,
#     "유로"  : 1268,
#     "위안"  : 171
# }

# num, currency = out.split()
# print(float(num) * transe[currency],'원')

# out1 = input('입력 1: ')
# out2 = input('입력 2: ')
# out3 = input('입력 3: ')

# print(max(float(out1), float(out2), float(out3)))

# out = input('입력 : ')

# tel = {
#     "011" : "SKT",
#     "016" : "KT",
#     "019" : "LGU",
#     "010" : "알수없음"
# }

# check, *_ = out.split('-')
# if check == '010':
#     print(tel['010'])
# else:
#     print(tel[check])

# out = input('입력 : ')
# post = {
#     "강북구" : ['010','011','012'],
#     "도봉구" : ['013','014','015'],
#     "노원구" : ['016','017','018','019']
# }

# if out[:3] in post.get('강북구'):
#     print('강북구')
# elif out[:3] in post.get('노원구'):
#     print('노원구')
# else:
#     print('도봉구')


# s_code = out.split('-')[1][0]

# if s_code == '1' or s_code == '3':
#     print('남자')
# elif s_code == '2' or s_code == '4':
#     print('여자')
    
# out = input('입력 : ')

# fir = (int(out[0])*2 + int(out[1])*3 + int(out[2])*4 + int(out[3])*5 + int(out[4])*6 + int(out[5])*7 + int(out[7])*8
#     + int(out[8])*9 + int(out[9])*2 + int(out[10])*3 +int(out[11])*4 +int(out[12])*5 ) % 11
# sec = 11 - fir

# if sec == int(out[13]):
#     print('맞음')
# else:   
#     print('틀림')   

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

# print(btc)

# max_price = float(btc['max_price'])
# min_max_gap = max_price - float(btc['min_price'])
# opening_sum_gap = float(btc['opening_price']) + min_max_gap

# if opening_sum_gap > max_price:
#     print('상승장')
# else:
#     print('하락장')

# list1 = [100,200,300]

# for x in list1:
#     print(x+x*0.1)

# list1 = ["SK하이닉스", "삼성전자", "LG전자"]
# for x in list1:
#     print(len(x))

# list2 =  ['intra.h', 'intra.c', 'define.h', 'run.py']

# for x in list2:
#     if x.split('.')[1] == 'h' or x.split('.')[1] == 'c':
#         print(x)

# for x in range(2002, 2051, 4):
#     print(x)

# result = 0
# for x in range(1,11):
#     if x % 2 == 1:
#         result += x
# print(result)

# price_list = [32100, 32150, 32000, 32500]

# for i, x in enumerate(price_list):
#     print(i, x)

# for x in range(len(price_list)):
#     print(len(price_list)-x-1, price_list[x])

# for i,data in enumerate(price_list):
#     if i > 0:
#         print(str((i-1)*10+100), data)

# my_list = ["가", "나", "다", "라", "마"]

# for x in range(len(my_list) - 2):
#     for y in range(3):
#         print(my_list[x+y], end=' ')
#     print()

# my_list = ["가", "나", "다", "라"]
# for x in range(len(my_list) -1):
#     print(my_list[len(my_list)-x-1], my_list[len(my_list)-x-2])


# my_list = [100, 200, 400, 800]
# for x in range(len(my_list) - 1):
#     print(my_list[x+1] - my_list[x])

# my_list = [100, 200, 400, 800, 1000, 1300]

# for x in range(len(my_list)-2):
#     print((my_list[x]+my_list[x+1]+my_list[x+2])/3)

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])

li1 = [3,1,4,5,2]

print([0] * x for x in li1)

dic1 = {'a' : 10}
dic1['b'] = 20

print(dic1)

dic1.setdefault('c', 30)

keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

y = dict.fromkeys(keys, 100)
print(y)

from collections import defaultdict

y = defaultdict(int)
print(y['s'])

p1 = defaultdict(lambda : 'ss')
print(p1['f'])

x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

# 키만 가져옴
xx = {key: 0 for key in dict.fromkeys(['a','b','c','d']).keys()}
print(xx)

yy = {value: 0 for value in {'a':10,'b':20,'c':30,'d':30}.values()}
print(yy)

dic2 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print({key: value for key, value in dic2.items() if value != 20})
