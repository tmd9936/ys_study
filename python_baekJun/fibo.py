def fibo(num):
    if num < 2:
        return num
    return fibo(num-1) + fibo(num-2)
    

out = int(input())
print(fibo(out))

