import sys

input = sys.stdin.readline

li = list()
for _ in range(int(input().strip())):
    out = input().strip()
    li.append(int(out))

num = 1
result_list = []
stack = []
point = -1
idx = 0
fail_check = False

while idx < len(li):
    result_list.append('+')
    stack.append(num)
    point += 1
    num += 1
    while point >= 0 and stack[point] >= li[idx]:
        result_list.append('-')
        point -= 1
        if stack.pop() == li[idx]:
            idx += 1
            continue
        fail_check = True
        
    if fail_check:
        print('NO')
        break
else:
    for r in result_list:
        print(r)
