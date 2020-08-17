li = []

import sys

input=sys.stdin.readline

for _ in range(int(input().strip())):
    out = input().strip()
    
    if ' ' in out:
        out = out.split(' ')
        li.append(out[1])
    else:
        if out == 'pop':
            if not li:
                print(-1)
            else:
                print(li.pop())
        elif out == 'top':
            if not li:
                print(-1)
            else:
                print(li[len(li)-1])
        elif out == 'empty':
            if not li:
                print(1)
            else:
                print(0)
        elif out == 'size':
            print(len(li)) 