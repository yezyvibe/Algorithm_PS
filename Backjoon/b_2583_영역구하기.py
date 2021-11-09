def dfs(x, y):
    global cnt, territory
    stack.append((x,y))
    territory = 1
    while stack:
        x, y = stack.pop()
        arr[x][y] = '0'
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    territory += 1
                    stack.append((nx, ny))
                    arr[nx][ny] = '0'
    cnt += 1
    result[cnt] = territory

m, n , k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
stack = []
cnt = 0
result = {}

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dfs(i, j)

result = list(result.values())
result.sort()
print(cnt)
print(' '.join(map(str, result)))