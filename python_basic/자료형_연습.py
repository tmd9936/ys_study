# 자료형 연습문제 

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print('apple','orange','banana','lemon',sep=';')

# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
s1 = "30"
print(int(s1))
print(float(s1))
print(complex(s1))
print(str(s1))


# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
s2 = "Niceman"
print(s2[4:])


# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
s3 = 'Strawberry'
print(s3[::-1])
print(''.join(list(reversed(s3))))

s3_t = ''
for x in s3:
    s3_t = x + s3_t
print(s3_t)


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
s4 = '010-7777-9999'
# print(''.join(s4.split('-')))
print(s4.replace('-',''))
# 정규표현식(Regular Expression)
import re
print(re.sub('[^0-9]','',s4))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
s5 = "http://daum.net"
#s5 = '' + s5[7:]
#print(s5.replace('http://', ''))

# daum.net
urlIdx = s5.index('http://')
print(s5[urlIdx + 7:])

# http://
urlIdx2 = s5.index('daum.net')
print(s5[urlIdx:urlIdx2])

# daum
urlIdx3 = s5.index('.net')
print(s5[urlIdx2:urlIdx3])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
s6 = "NiceMan"
print(s6.upper())
print(s6.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
s7 = "abcdefghijklmn"
print(s7[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
s8 = ["Banana", "Apple", "Orange"]
del s8[1]
s8_2 = ["Banana", "Apple", "Orange"]
s8_2.remove("Apple")
print(s8)
print(s8_2)


# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
s9 = (1,2,3,4)
print(list(s9))
print([x for x in s9])


# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
s10 = {
    '성인'  :   '100000',
    '청소년':   '70000',
    '아동'  :   '30000',
}
print(s10)


# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
s10['소아'] = '0'
print(s10)


# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(list(s10.keys()))


# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(list(s10.values()))


# *** 결과 값만 정확하게 출력되면 됩니다. ^^
