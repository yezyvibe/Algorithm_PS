import sys
from collections import deque

# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
def bfs(a, b, moving, baby_shark):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(a, b, 0)])
    visit = [[0]*n for _ in range(n)]
    visit[a][b] = 1
    eatable = []
    while q:
        x, y, dis = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if arr[nx][ny] <= baby_shark[0]: # 아기 상어가 지나갈 수 있는 경우
                    q.append((nx, ny, dis + 1))
                    visit[nx][ny] = 1
                    if 0 < arr[nx][ny] < baby_shark[0]: # 먹을 수 있는 경우
                        eatable.append((nx, ny, dis + 1))
    if eatable:
        eatable.sort(key = lambda x : (x[2], x[0], x[1]))
        moving += eatable[0][2]
        cur_x, cur_y = eatable[0][0], eatable[0][1]
        arr[cur_x][cur_y] = -1
        baby_shark[1] += 1
        if baby_shark[0] == baby_shark[1]:
            baby_shark = [baby_shark[0]+1, 0]
        return bfs(cur_x, cur_y, moving, baby_shark)  # 아기 상어가 잡아 먹는 물고기
    return moving

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
baby_shark = [2, 0]
moving = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = -1
            print(bfs(i, j, moving, baby_shark))
        