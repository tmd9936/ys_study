import sys

input = sys.stdin.readline


for _ in range(int(input().strip())):
    words = input().strip().split()
    for word in words:
        for s in word[::-1]:
            print(s, end='')
        print(' ',end='')
    print()
