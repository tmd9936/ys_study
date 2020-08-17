out = input('더미')

import math

out = input().split(' ')

first = int(out[0])
max_length = math.ceil(math.sqrt(int(out[1])))
prime_check = [False,False] + [True]*(int(out[1])-1)


for i in range(2, max_length+1):
    if prime_check[i]:
        for j in range(i+i, int(out[1])+1, i):
            prime_check[j] = False

for i, check in  enumerate(prime_check[first:]):
    if check:
        print(i+first)
    


        
