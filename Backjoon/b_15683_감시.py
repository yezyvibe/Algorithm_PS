from copy import deepcopy
import sys

def office(x, y, temp, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 6:
                    break
                elif temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
            else:
                break

def dfs(arr, cnt):
    global min_v
    temp = deepcopy(arr)
    if cnt == cctv_cnt:
        res = 0
        for i in range(n):
            res += temp[i].count(0)
        min_v = min(min_v, res)
        return
    x, y, cctv = cctv_lst[cnt]
    for d in directions[cctv]:
        # 유효 방향은 모두 탐색
        office(x, y, temp, d)
        dfs(temp, cnt+1)
        temp = deepcopy(arr)

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 하 상 우 좌
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# 1~5번까지 방향 정의
directions = [
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[3,0], [0, 2], [2, 1], [1, 3]],
    [[1,3,0],[3,0,2],[0,2,1],[2,1,3]],
    [[0, 1, 2, 3]]
    ]

min_v = 100000000
cctv_lst = []
cctv_cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv_lst.append([i, j, arr[i][j]])
            cctv_cnt += 1

dfs(arr, 0)
print(min_v)

