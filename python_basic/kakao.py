board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    basket = []
    answer = 0
    for move in moves:
        for idx in range(0,len(board)):
            if  board[idx][move-1] > 0:
                basket.append(board[idx][move-1])
                board[idx][move-1] = 0
                if len(basket) >= 2:
                    if basket[len(basket)-1] == basket[len(basket)-2]:
                        basket.pop()
                        basket.pop()
                        answer += 1
                break
    return answer

print(solution(board, moves))

