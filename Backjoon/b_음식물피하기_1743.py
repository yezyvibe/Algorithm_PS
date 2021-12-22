import sys


def dfs(i, j):
    s = [(i, j)]
    visit[i][j] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    cnt = 1
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visit[nx][ny]:
                visit[nx][ny] = 1
                cnt += 1
                s.append((nx, ny))

    return cnt

input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
arr = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
answer = 0

for i in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visit[i][j]:
            answer = max(answer, dfs(i, j))
print(answer)