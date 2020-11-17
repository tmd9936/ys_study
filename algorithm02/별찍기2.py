from sys import stdin

k = int(stdin.readline())
arr = [[' ' for _ in range(k)] for _ in range(k)]


def star10(x, y ,num):
    if num == 1:
        arr[x][y]='*'
        return
    
    div = int(num/3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            else:
                star10(div*i+x, div*j+y, div)

star10(0,0,k)

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="")
    if i < len(arr) - 1:
        print()

