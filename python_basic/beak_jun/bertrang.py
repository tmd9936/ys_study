out = input('더미')

import math

def prime_check(num):
    max_num = num*2
    is_prime = [False,False] + [True]*(max_num-1)

    max_mul_num = math.ceil(math.sqrt(max_num)) if num != 2 else math.ceil(math.sqrt(max_num))+1
    
    for i in range(2, max_mul_num):
        if is_prime[i]:
            for j in range(i*2, max_num+1, i):
                is_prime[j] = False
    
    result = 0
    for number in is_prime[num+1:]:
        if number:
            result += 1
    print(result)

out_list = []
while True:
    out = input()
    if out == '0':
        break
    out_list.append(int(out))
    
for out in out_list:    
    prime_check(out)



