# copy와 deepcopy
# 싱글 리스트일 경우
list1 = [1,2,3,4]
list2 = list1.copy()
list2[1] = 100
print(list1)
print(list2)
# copy 결과 -> 둘이 같이 안 바뀜

# 중첩 리스트일 경우
list_x = [[1,2,3],[4,5,6,],[7,8,9]]
list_y = list_x.copy()
list_y[1][1] = 100
print(list_x)
print(list_y)
# copy 결과 -> 둘이 같이 바뀜
import copy
list_m = [[1,2,3],[4,5,6,],[7,8,9]]
list_n = copy.deepcopy(list_m)
list_n[1][1] = 100
print(list_m)
print(list_n)
# copy.deepcopy() 결과 -> 같이 안 바뀜



# 싱글 dictionary의 경우
dict_x = {'a':1, 'b':2, 'c':3}
dict_y = dict_x.copy()
dict_y['a'] = 100
print(dict_x)
print(dict_y)
# copy의 결과 -> 둘이 같이 안 바뀜

from collections import defaultdict

t = (1,2,3,4,5)
dictx = dict.fromkeys(t)
dictx = defaultdict(int)
print(dictx)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = list(map(lambda x : str(x) if x % 3 ==0 else x, a))
print(a2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a3 = list(map(lambda x : str(x) if x == 1 else float(x) if x ==2 else x+10, a))
print(a3)


a = {1,2,3,4}
b = {3,4,5,6}

print(a|b)
print(set.union(a,b))
print(a&b)
print(a-b)
print(a^b)

a = {1,2,3,4}
b = {3,4,5,6}
c = {8,9,10,11}

print(a <= {1, 2, 3, 4})
print(a < {1, 2, 3, 4, 5})
print(a > {1,2,3,4})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

