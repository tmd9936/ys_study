def solution(n):
    answer = ''
    # 점화식? dp인거 같음;
    is_first = True
    is_zero = False
    while True:
        num = int(n%3)
        if is_first and num == 0:
            n -= 1
            num = int(n%3)
            is_zero = True
        answer += str(num)
        n = int(n/3)
        if n <= 0:
            break
        is_first = False
    if is_zero:
        answer = str(int(answer) + 2)
    return answer

def solution1(n):
    answer = ''
    # 점화식? dp인거 같음;
    while True:
        is_zero = False
        num = int(n%3)
        if  num == 0:
            n -= 1
            num = int(n%3)
            is_zero = True
        answer += str(num)
        n = int(n/3)
        if n <= 0:
            break
        if is_zero:
            answer = str(int(answer) + 2)
    answer = ''.join([x for x in answer[::-1]])
    return answer

print(solution1(513))