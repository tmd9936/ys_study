# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo (n-2)

# def fibo2(n):
#     cache = [0]*int(n)
#     cache[0] = 0
#     cache[1] = 1

#     for x in range(2, n):
#         cache[x] = cache[x-1] + cache[x-2]
#     return cache


# print(fibo2(10))

def cut_rod(n):
    p = [0,1,5,8,9,10,17,17,20,24,30]
    r = [0]
    if n == 0:
        return 0;
    if n >= 1:
        pass


print(cut_rod(7))