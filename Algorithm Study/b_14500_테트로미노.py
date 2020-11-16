import sys


def dfs(i, j, cnt, sum_v):
    global max_v

    if cnt == 4:
        max_v = max(max_v, sum_v)
        return

    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum_v + arr[nx][ny])
            visit[nx][ny] = 0


def middleFinger(x, y):
    global max_v

    middle = [
        [(-1, 0), (0, -1), (0, 0), (0, 1)],  # ㅗ
        [(0, -1), (0, 0), (0, 1), (1, 0)],  # ㅜ
        [(0, -1), (-1, 0), (0, 0), (1, 0)],  # ㅓ
        [(-1, 0), (0, 0), (1, 0), (0, 1)]  # ㅏ
    ]
    tmp = 0
    for c in range(4):
        for k in range(4):
            nx, ny = x + middle[c][k][0], y + middle[c][k][1]
            if 0 <= nx < n and 0 <= ny < m:
                tmp += arr[nx][ny]
            else:
                tmp = 0
                break
        else:
            max_v = max(max_v, tmp)
            tmp = 0
    return


input = sys.stdin.readline
n, m = map(int, input().split(' '))
arr = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
max_v = 0
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        middleFinger(i, j)
        visit[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visit[i][j] = 0
print(max_v)
