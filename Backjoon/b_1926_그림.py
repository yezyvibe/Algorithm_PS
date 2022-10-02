import sys

def dfs(a, b, visit):
    stack = [(a, b)]
    visit[a][b] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n, m = len(visit), len(visit[0])
    area = 1
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    stack.append((nx, ny))
                    area += 1
    return area
    
input = sys.stdin.readline
n, m = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
cnt_area = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visit[i][j]:
            cnt_area += 1
            max_area = max(dfs(i, j, visit), max_area)
print(cnt_area)
print(max_area)
