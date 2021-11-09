# 최소 이동 횟수 -> bfs
import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]  # 위부터 아래로


def bfs(a, b, ga, gb):
    q = deque([(a, b)])
    bg[a][b] = 0
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not bg[nx][ny]:
                q.append((nx, ny))
                bg[nx][ny] = bg[x][y] + 1
                if nx == ga and ny == gb:
                    return bg[nx][ny]


for tc in range(int(input().rstrip())):
    n = int(input())
    bg = [[0] * n for _ in range(n)]
    a, b = map(int, input().split(' '))
    ga, gb = map(int, input().split(' '))
    if a == ga and b == gb:
        print(0)
    else:
        print(bfs(a, b, ga, gb))
