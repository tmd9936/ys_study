from sys import stdin

k = int(stdin.readline())

min_num = k

for r in range(1,k-1):
    sum_num = 0
    temp = r
    while True:
        share = temp // 10
        rem = temp % 10
        sum_num += rem
        temp = share
        if share <= 0:
            break
    
    if k == sum_num + r and min_num >= sum_num + r:
        min_num = r
    
if min_num == k:
    print(0)
else:
    print(min_num)

    
    

            
