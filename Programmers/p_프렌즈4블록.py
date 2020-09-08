def four_blocks(m, n, board):
    visit_set = set()
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i - 1][j - 1] == board[i - 1][j] == board[i][j - 1] != '_':
                visit_set |= set([(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)])

    # 2x2가 되는 애들은 1로 표시
    for i, j in visit_set:
        board[i][j] = 1
    # 1인 애들은 '_'로 대체하고 맨 앞으로 옮기는 것처럼 구현
    for idx, row in enumerate(board):
        tmp = ['_'] * row.count(1)
        board[idx] = tmp + [b for b in row if b != 1]
    return len(visit_set)


def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))  # 행열 뒤집기
    while True:
        res = four_blocks(m, n, board)
        if res == 0:
            return answer
        answer += res