from collections import deque


def bfs(t_q):
    day = 0
    while t_q:
        x, y = t_q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                t_q.append((nx, ny))
        day = box[x][y]
    for t in box:
        if 0 in t:
            day = 0
            break
    return day - 1


m, n = map(int, input().split(' '))  # m열 n행
box = [list(map(int, input().split(' '))) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
t_q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            t_q.append((i, j))

print(bfs(t_q))
