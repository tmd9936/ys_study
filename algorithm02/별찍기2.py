k = 9
arr = [[" "]*k for i in range(k)]



def star1(s):
    k = len(s)
    for i in range(len(s)):
        for j in range(len(s)):
            if (i >= int(k/3) and i < k-int(k/3)) and ((j >= int(k/3) and j < k-int(k/3))):
                arr[i][j] = "#"
            else:
                arr[i][j] = "*"

def star(k):
    if k == 1:
        arr = [["*"]*1 for i in range(1)]
        return arr
    for i in range(3):
        for j in range(3):
            if cnt == 5:
                arr[i][j] = "#"
            else:
                arr[i][j] = "*"
            cnt += 1
        


for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="")
    print()

