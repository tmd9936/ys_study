from sys import stdin

k = int(stdin.readline())


# start에서 via를 거쳐 to로 보내기
def hanoi(n, start, to, via):
    if n == 1:
        print(start, to)
        #log.append([start, to])
    else:
        hanoi(n-1, start, via, to)
        #log.append([start, to])
        print(start, to)
        hanoi(n-1, via, to, start)

print(2**k-1)
if k <=20:
    hanoi(k,'1','3','2')

# for i in range(0, len(log)):
#     if i != len(log) -1:
#         print(log[i][0], log[i][1])
#     else:
#         print(log[i][0], log[i][1], end="")
        
