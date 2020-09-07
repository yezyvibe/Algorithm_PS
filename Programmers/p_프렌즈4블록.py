dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    tmp = board[i][j]
    stack = [(i, j)]

    while stack:
        a, b = stack.pop()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < m and 0 <= ny < n:
                next = board[nx][ny]
                if next == tmp:



def solution(m, n, board):
    answer = 0
    for i in range(m):
        for j in range(n):
            dfs(i, j)

    return answer