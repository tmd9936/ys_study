def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

out = int(input())
print(factorial(out))

