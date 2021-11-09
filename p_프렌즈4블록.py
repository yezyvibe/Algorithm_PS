def four_blocks(m, n, board):
    visit_set = set()
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i][j-1] == board[i-1][j] == board[i-1][j-1] != '-':
                visit_set.update(set([(i,j), (i, j-1), (i-1, j), (i-1, j-1)]))

    for i, j in list(visit_set):
        board[i][j] = 1
    
    for idx, row in enumerate(board):
        tmp = ['-']*row.count(1)
        board[idx] = tmp + [ i for i in row if i != 1]
    return len(visit_set)

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while True:
        res = four_blocks(m, n, board)
        if res == 0:
            return answer
        answer += res
    
    



m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))