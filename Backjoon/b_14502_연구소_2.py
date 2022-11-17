from itertools import combinations as combi
import sys


def dfs(i, j, arr, visit):
    m, n = len(arr[0]), len(arr)
    stack = [(i, j)]
    visit[i][j] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if not visit[nx][ny] and not arr[nx][ny]: # 방문하지 않았고, 빈칸이어야 바이러스가 퍼질 수 있다.
                    visit[nx][ny] = 1
                    stack.append((nx, ny))

    return visit


def checkSafeZone(visit):
    cnt = 0
    for i in range(len(visit)):
        for j in range(len(visit[0])):
            if not visit[i][j]:
                cnt += 1
    return cnt

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

candi = []
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            candi.append((i, j))

for c in combi(candi, 3):
    for a, b in list(c):
        arr[a][b] = 1 # 칸을 임시로 두고

    visit = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                visit = dfs(i, j, arr, visit)
            elif arr[i][j] == 1:
                visit[i][j] = 1
    
    result = checkSafeZone(visit)
    answer = max(answer, result)

    for a, b in list(c):
        arr[a][b] = 0 # 두었던 칸 다시 원상복구
print(answer)