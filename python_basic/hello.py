

print('Hello python!!')
print('Hello python!!')
print()
word = "Py"

print(word + 'thon')
word = word + 'thon'

print(word[0])
print(word[1])
print(word[-1])
print(word[-2])

# separator 옵션
# sep의 기본값 sep=' '
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='/')
print('T', 'E', 'S', 'T', sep='')
print('2020', '7', '14', sep='-')
print('test', 'naver.com', sep='@')

print('------------ end 옵션 --------------')

# end 옵션 기본값 end='\n'
print('welcome To', end=' ')
print('Test')

print('%s의 나이는 %d' % ("홍길동", int(33)))

# format 사용
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} and {var2} and {var1}'.format(var1='You', var2='Me'))
print('{0} is word'.format(word))
print('Test1: %5d, Price: %4.2f' % (766, 43221.544))

''' 
Escape 코드
\n : 개행
\t : tap
\\ : 역슬래쉬
\' : 작은따옴표

str 문자열
int 정수
float 실수
complex 복소수
bool 불린

list 리스트
tuple 튜플
set 집합
dict 사전
'''
print('----------------- 문자열 ---------------')
# 데이터 타입(Data Type)
v_str1 = "Good morning"
v_bool = True
v_str2 = "Good night"
v_float = 10.0
v_int = 7
v_list = [v_str1, v_str2]
v_tuple = 3, 6, 8
v_dic = {
    "name": "홍길동",
    "age": 28
}
v_set = {7, 8, 9}

# 데이터 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_list))
print(type(v_dic))
print(type(v_tuple))
print(type(v_set))

'''
변수 이름 규칙

숫자로 시작하는 변수 이름 x
변수는 소문자로 시작하는 것이 관례

예억어 사용할 수 없다 ex) tuple, class, def, int, float

'''

'''
숫자형 연산자
+,-,*,/,%(나머지 연산자),//()
abs(x) 절대값
pow
x**y x의 y제곱
'''
print(10%3)
print('%.3f' %(10/3)) # 정수형
print(10//3) # 실수형
print(abs(-10))

# 정수 선언
i = 77
ii = -45
big_int = 999999999999999999999
print(i)
print(ii)
print(big_int)

# 실수 선언
f = 0.3455
ff = -1.4566
print(f)
print(ff)
print('i + ii = ', i + ii)
print('f + ff = ', f + ff)
print('i + ff = ', i + ff)

# 자료형(type)
print(type(i), type(f))

print('-------------형변환-------------')
# 형변환(casting)
# int, float, complex
a = 5.
b = 4
c = 10
result = a+b
print(result)
print(int(result)) # 정수
print(float(c)) # 실수
print(complex(3)) # 복소수
print(int(True)) # bool -> 정수
print(int(False)) # bool -> 정수
print(int('3')) # 문자 -> 정수

#수치연산 함수
print(abs(-7)) # 절대값

n7, m7 = divmod(100, 8)
print(n7, m7)

import math
'''
ceil() 올림
floor() 내림
round() 반올림
'''
print(math.ceil(5.3)) 
print(math.floor(4.5))
print(round(30.4))
print(round(30.7))
