from sys import stdin

k = int(stdin.readline())

tower = [[x for x in range(k, 0, -1)] for _ in range(3)]

for i in range(1,3):
    for j in range(k):
        tower[i][j] = 0


print(tower)

# def hanoi():