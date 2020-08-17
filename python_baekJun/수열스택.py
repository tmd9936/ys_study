import sys

input = sys.stdin.readline

li = list()
for _ in range(int(input().strip())):
    out = input().strip()
    li.append(int(out))

num = 1
result_list = []
stack = [1]
point = 0
fail_check = False
for check_num in li:
    while True:
        if point == -1 or stack[point] < check_num:
            result_list.append('+')
            stack.append(num)
            point += 1
            num += 1
        elif stack[point] >= check_num:
            result_list.append('-')
            if check_num not in stack:
                fail_check = True
                break
            if point >= 0:
                point -= 1
            if stack.pop() == check_num:
                break
    if fail_check:
        print('NO')
        break
else:
    for r in result_list:
        print(r)
