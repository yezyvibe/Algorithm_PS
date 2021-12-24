import sys

def dfs(i, j):
    s = [(i, j)]
    visit[i][j] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    team = arr[i][j]
    cnt = 1
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                if team == arr[nx][ny]:
                    s.append((nx, ny))
                    visit[nx][ny] = 1
                    cnt += 1
    return [team, cnt]

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
visit = [[0]*n for _ in range(m)]
power = {'W':0, 'B':0}
for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            team, cnt = dfs(i, j)
            power[team] += cnt**2
print(str(power['W'])+' '+str(power['B']))