from sys import stdin

#inp = stdin.readline().split(" ")

# num = int(inp[0])
# limit_num = int(inp[1])

#nums = list(map(int,stdin.readline().split(" ")))

num = 5
limit_num = 21
nums = [5,6,7,8,9]

result = 

def comb(lis, n):
    rst = []
    if n > len(lis):
        return rst
    elif n == 1:
        for i in lis:
            rst.append([i])
    elif n > 1:
        for i in range(len(lis)-n+1):
            for temp in comb(lis[i+1:], n-1):
                rst.append([lis[i]]+temp)

    return rst


def comb2(lis, n):
    rst = []
    for i in range(len(lis)):
        if n==1:
            yield lis[i]
        else:
            for temp in comb2(lis[i+1:len(lis)], n-1):
                yield lis[i] + temp



# print(check(nums,limit_num))