import sys
from collections import deque


input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
q_j = deque()
q_f = deque()
visit_j = [[0] * c for _ in range(r)]
visit_f = [[0] * c for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = []


for i in range(r):
    for j in range(c):
        if arr[i][j] == 'F':
            q_f.append((i, j))
        elif arr[i][j] == 'J':
            q_j.append((i, j))

while q_f:
    x, y = q_f.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            if not visit_f[nx][ny] and arr[nx][ny] == '.':
                visit_f[nx][ny] = visit_f[x][y] + 1
                q_f.append((nx, ny))

while q_j:
    x, y = q_j.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]

        # 범위 밖
        if not (0 <= nx < r and 0 <= ny < c):
            print(visit_j[x][y] + 1)
            sys.exit()
        
        # 범위 안
        if not visit_j[nx][ny] and arr[nx][ny] == '.':
            if not visit_f[nx][ny] or visit_j[x][y] + 1 < visit_f[nx][ny]:
                visit_j[nx][ny] = visit_j[x][y] + 1
                q_j.append((nx, ny))

print('IMPOSSIBLE')