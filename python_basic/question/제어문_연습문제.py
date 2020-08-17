# 제어문 연습문제

# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print(q1['가을'])
for k,v in q1.items():
    if k == '가을':
        print(v)


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# print(q2.get('가을'))
for k, v in q2.items():
    if v == '사과':
        print(k,v)
        break
else:
    print('사과없음')
print()

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.(점수는 임의로 지정하여 테스트)
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

grade = 67

if grade > 80:
    print('A학점')
elif grade > 60:
    print('B학점')
elif grade > 40:
    print('C학점')
elif grade > 20:
    print('D학점')
else:
    print('E학점')


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18

_max = a

if b > a:
    _max = b
elif c > b:
    _max = c
print(_max)

li = [12,6,18]
_max2 = li[0]
for x in li:
    if x > _max2:
        _max2 = x
print(_max2)



# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-1473837'
s_test = s[7]

if s_test == '1' or s_test == '3':
    print('남자')
else:
    print('여자')


# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q3 = ["갑", "을", "병", "정"]

for x in q3[:3]:
    print(x, end=' ')
print()
print([x for x in q3[:3]])


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)

for x in range(1, 101, 2):
    print(x, end =' ')
print()
print([x for x in range(1,101,2)])


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
print([x for x in q4 if len(x) >= 5])

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print([x for x in q5 if x.islower()])

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
# (List Comprehension 방식 일반 방식 모두 이용해보세요.)
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for x in q6:
    if x.isupper():
        print(x.lower(), end=' ')
    else:
        print(x.upper(), end=' ')
print()

print([x.upper() if x.islower() else x.lower() for x in q6])

#### test

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [ i if i>0 else 0 for i in original_prices]
print(prices)

print({i*j for i in range(2,4) for j in range(2,10) if i*j % 2 == 0 and i*j % 3 == 0})

subjects = ['math', 'history', 'english', 'computer engineering']
scores = [90, 80, 95, 100]

print({x: y for x,y in zip(subjects, scores)})

ces = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16, 0, 14.99]
test1 = [{'zero' : x} if x == 0 else {'plus' : x} if x >= 0 else {'minus' : x}  for x in ces if x > 10 or x <= 0]
print(test1)
