k = 9
arr = [[' ' for _ in range(k)] for _ in range(k)]



# def star1(s):
#     k = len(s)
#     for i in range(len(s)):
#         for j in range(len(s)):
#             if (i >= int(k/3) and i < k-int(k/3)) and ((j >= int(k/3) and j < k-int(k/3))):
#                 arr[i][j] = "#"
#             else:
#                 arr[i][j] = "*"

# def star(k):
#     if k == 1:
#         arr = [["*"]*1 for i in range(1)]
#         return arr
#     else:
#         cnt = 0
#         for i in range(3):
#             for j in range(3):
#                 if cnt == 4:
#                     arr[i][j] = "0"
#                 else:
#                     arr[i][j] = "*"
#                 cnt += 1


# https://blog.naver.com/PostView.nhn?blogId=repeater1384&logNo=222090302711

def star2(k):
    if k == 1:
        arr = [["*"]*1 for i in range(1)]
    else
        cnt = 0
        for i in range(3):
            for j in range(3):
                if cnt == 4:
                   


for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end="")
    print()

