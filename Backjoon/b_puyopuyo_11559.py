import sys
from collections import deque
from types import resolve_bases


def bfs(i, j):
    q = deque([(i, j)])
    visit[i][j] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny]:
                if arr[nx][ny] == arr[x][y]:
                    cnt += 1
                    visit[nx][ny] = 1
                    q.append((nx, ny))
    if  cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visit[i][j]:
                    arr[i][j] = '.'
        else:
            return True
    return False

def change_arr():
    for i in range(6):   # 열
        queue = deque()
        for j in range(11, -1, -1): # 행 끝에서부터
            if arr[j][i] != '.':
              queue.append(arr[j][i])  # 색깔인 경우 queue에 넣기
        for j in range(11, -1, -1):
            if queue:
                arr[j][i] = queue.popleft()
            else:
                arr[j][i] = '.'

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = [list(input().rstrip()) for _ in range(12)]
answer = 0
while True:
    chk = 0
    visit = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visit[i][j]:
                visit[i][j] = 1
                res = bfs(i, j)
                if res:
                    chk = 1
    if not chk:
        break
    change_arr()
    answer += 1
print(answer)