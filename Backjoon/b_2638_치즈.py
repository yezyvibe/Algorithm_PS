import sys
from collections import deque


def bfs():
    q = deque([])
    q.append((0, 0))
    visit[0][0] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if arr[nx][ny] >= 1:
                    # 얼마나 공기에 접촉했는지 표시
                    arr[nx][ny] += 1
                else:
                    visit[nx][ny] = 1
                    q.append((nx, ny))

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0

while True:
    visit = [[0]*m for _ in range(n)]
    bfs()
    flag = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0 # 치즈 없애기
                flag = True
            elif arr[i][j] == 2:
                arr[i][j] = 1 # 다시 치즈 초기화    

    if not flag:
        # 더 이상 치즈가 없다
        print(time)
        break
    time += 1