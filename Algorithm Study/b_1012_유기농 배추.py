import sys


def dfs(i, j):
    global cnt
    s = [(i, j)]
    bg[i][j] = cnt
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and bg[nx][ny] == -1:
                bg[nx][ny] = cnt
                s.append((nx, ny))
    cnt += 1


input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for tc in range(int(input())):
    m, n, k = map(int, input().rstrip().split(' '))
    bg = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split(' '))
        bg[x][y] = -1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if bg[i][j] == -1:
                dfs(i, j)
    print(cnt)
