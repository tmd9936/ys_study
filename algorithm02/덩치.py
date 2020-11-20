from sys import stdin

n = int(stdin.readline())

mans =[]

for _ in range(n):
    m = stdin.readline().split(' ')
    mans.append([int(m[0]), int(m[1]), 0])

for i in range(n):
    for j in range(n):
        if mans[i][0] > mans[j][0] and mans[i][1] > mans[j][1]:
            mans[i][2] += 1

for i in range(n):
    rank = 1
    for j in range(n):
        if mans[i][2] < mans[j][2]:
            rank += 1
    if i == n - 1:
        print(rank, end="")
    else:
        print(rank, end=" ")
