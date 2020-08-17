import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
    out = input().strip()
    l_count = 0

    for ps in out:
        if ps == '(':
            l_count += 1
        else:
            l_count -= 1
            if l_count < 0:
                print('NO')
                break
    else:
        if l_count != 0:
            print('NO')
        else:
            print('YES')
            
