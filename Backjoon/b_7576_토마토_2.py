# 최소 일수 -> bfs
import sys
from collections import deque

def check(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                return False # 아직 안 끝남
    return True

def bfs(tomato):
    q = deque(tomato)
    n, m = len(arr), len(arr[0])

    while q:
        x, y = q.popleft() 

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            # print(nx, ny, n, m, 'next')
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and arr[nx][ny] == 0:
                    visit[nx][ny] = 1
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

                    
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 1

tomato = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomato.append((i, j))
            visit[i][j] = 1

# print('tomato', tomato)
bfs(tomato)

if not check(arr):
    print(-1)
else:
    answer = max(map(max, arr)) - 1
    print(answer)


# for a in arr:
#     print(a)
# print()

