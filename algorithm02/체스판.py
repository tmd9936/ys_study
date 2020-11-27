from sys import stdin

m, n = stdin.readline().split(' ')
m, n = int(m), int(n)
chess = []

for _ in range(int(m)):
    chess_line = stdin.readline()
    chess.append(chess_line)

min_draw = m * n - 1
pre_color = "W"

for x in range(m-7):
    for y in range(n-7):
        for check in range(2):
            if check == 0:
                pre_color = "W"
            else:
                pre_color = "B"
            draw_cnt = 0
            for i in range(8):
                for j in range(8):
                    if pre_color == chess[i+x][j+y]:
                        draw_cnt += 1
                    
                    if j != 7:
                        if pre_color == "W":
                            pre_color = "B"
                        else:
                            pre_color = "W"

            if draw_cnt < min_draw:
                min_draw = draw_cnt

print(min_draw, end="")