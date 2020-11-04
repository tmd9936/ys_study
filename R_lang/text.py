from sys import stdin

inp = stdin.readline().split(" ")

num = int(inp[0])
limit_num = int(inp[1])

nums = stdin.readline().split(" ")


# def comb(lis, n):
#     rst = []
#     if n > len(lis):
#         return rst
#     elif n == 1:
#         for i in lis:
#             rst.append([i])
#     elif n > 1:
#         for i in range(len(lis)-n+1):
#             for temp in comb(lis[i+1:], n-1):
#                 rst.append([lis[i]]+temp)

#     return rst


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

a = c_max(nums, limit_num)

print(a)
