def dfs(x, y, cnt, sumVal):
    global maxVal
    if cnt == 4:
        maxVal = max(maxVal, sumVal)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(nx, ny, cnt+1, sumVal + arr[nx][ny])
                visit[nx][ny] = 0

def middlefinger(x, y):
    global maxVal
    for k in mfinger:
        try:
            sumVal = arr[x][y] + arr[x + k[0][0]][y + k[0][1]] + arr[x + k[1][0]][y + k[1][1]] + arr[x + k[2][0]][y + k[2][1]]
        except:
            sumVal = 0
        maxVal = max(sumVal, maxVal)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mfinger = [
    [[0,1],[0,2],[-1,1]],
    [[0,1],[0,2],[1,1]],
    [[1,0],[2,0],[1,1]],
    [[1,0],[2,0],[1,-1]]
]
maxVal = 0

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visit[i][j] = 0
        middlefinger(i, j)

print(maxVal)