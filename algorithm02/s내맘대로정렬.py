def solution(strings, n):
    answer = []
    min_len = min([len(st) for st in strings])
    
    answer = sorted(strings, key=lambda st: tuple([st[a] for a in range(n, min_len)]))
    
    temp = ""
    for i in range(0,len(answer) - 1):
        if answer[i][n] == answer[i+1][n]:
            min_l = min([len(answer[i+1]), len(answer[i])])
            for j in range(n+1, min_l):
                if (answer[i][j] != answer[i+1][j]):
                    if answer[i+1][j] < answer[i][j]:
                        temp = answer[i]
                        answer[i] = answer[i+1]
                        answer[i+1] = temp
                        break
        
        
    
    return answer

if 'a' > 'b':
    print(1)
else:
    print(2)

["abzcd","cdzab","abafg","abzaa","abzbb","bbzaa"]
["abafg","abzaa","abzbb","abzcd","bbzaa","cdzcb",]