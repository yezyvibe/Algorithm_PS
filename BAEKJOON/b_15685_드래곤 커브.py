import sys

input = sys.stdin.readline

n = int(input())
arr = [[0]*101 for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
for i in range(n):
    x, y, d, g = map(int, input().rstrip().split(' '))
    arr[x][y] = 1
    dir = [d]
    for _ in range(g):
        tmp = [(i + 1) % 4 for i in dir[::-1]]
        dir.extend(tmp)

    for k in dir:
        nx, ny = x + dx[k], y + dy[k]
        arr[nx][ny] = 1
        x, y = nx, ny

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] == 1:
            cnt += 1
print(cnt)
