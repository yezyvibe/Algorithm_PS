def solution(board, moves):
    n = len(board)
    bg = [[0] * n for _ in range(n)]
    basket = [0]
    answer = 0

    # 배열 인덱스 순으로 바꾸기
    for i in range(n):
        for j in range(n):
            bg[i][j] = board[j][i]

    for move in moves:
        tmp = bg[move - 1]
        for k in range(n):
            number = tmp[k]
            if number == 0:
                pass
            else:
                if basket[-1] == number:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(number)
                bg[move-1][k] = 0
                break
    return answer



