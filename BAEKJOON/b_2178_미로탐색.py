import sys
from collections import deque

input = sys.stdin.readline

# 너비 우선 탐색
n, m = map(int, input().split(' '))
bg = [list(map(int, input().rstrip())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
d = deque()
d.append((0, 0))

while d:
    x, y = d.popleft()

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and bg[nx][ny] == 1:
            d.append((nx, ny))
            bg[nx][ny] = 1 + bg[x][y]
            if nx == n - 1 and ny == m - 1:
                print(bg[nx][ny])
                break
