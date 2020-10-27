from sys import stdin

inp = stdin.readline().split(" ")

num = int(inp[0])
limit_num = int(inp[1])

nums = list(map(int,stdin.readline().split(" ")))


def comb2(lis, n):
    rst = []
    for i in range(len(lis)):
        if n==1:
            yield lis[i]
        else:
            for temp in comb2(lis[i+1:len(lis)], n-1):
                yield lis[i] + temp

max_num = 0
for i in comb2(nums, 3):
    if i <= limit_num and i > max_num:
        max_num = i

def comb(lis,n):
    rst = []
    if len(lis) < n:
        return rst
    elif n == 1:
        for i in lis:
            rst.append([i])
    else:
        for i in range(len(lis)-n+1):
            for temp in comb(lis[i+1:], n-1):
                rst.append([lis[i]] + temp)

    return rst

print(comb(nums, 3))

