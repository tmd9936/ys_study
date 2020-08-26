def solution(strings, n):
    answer = []
    max_len = max([len(st) for st in strings])
    
    for idx in range(0, len(strings)):
        while len(strings[idx]) < max_len:
            strings[idx] = strings[idx] + '0'
    
    answer = sorted(strings, key=lambda st: tuple([st[a] for a in range(n, max_len)]))

    for i in range(0, len(answer)):
        if answer[i][len(answer[i])-1] == '0':
            for j in range(len(answer[i])-1, -1, -1):
                if answer[i][j] != '0':
                    answer[i] = answer[i][0:j+1]
                    break
    
    return answer