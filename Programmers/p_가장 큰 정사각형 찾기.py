def solution(board):
    r = len(board)
    c = len(board[0])
    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1

    res = []
    for r in board:
        res.append(max(r))
    return max(res)**2

    # arr = sum(board, [])
    # max_v = max(arr)
    # return max_v**2
