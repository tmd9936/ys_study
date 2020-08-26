
ss = "abcd"


def solution(s):
    # answer = len(s) % 2 == 0 if s[len(s) / 2] else s[len(s)/2-1:len(s)/2+1]
    ln = int(len(s) / 2)
    answer = s[ln] if len(s) % 2 == 1  else s[ln-1:ln+1]
    return answer



print(solution(ss))