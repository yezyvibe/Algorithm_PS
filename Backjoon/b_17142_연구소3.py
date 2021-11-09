from collections import deque
from itertools import combinations as combi
from itertools import chain

def bfs(virus):
    temp = [[-1]*n for _ in range(n)]
    q = deque()
    max_v = 0
    for i in virus:
        q.append(i)
        temp[i[0]][i[1]] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] != 1 and temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    if arr[nx][ny]==0:
                        max_v = max(max_v, temp[nx][ny])
                    q.append([nx, ny])
    # total1 = list(sum(temp,[]))
    # total2 = list(sum(arr,[]))
    total1 = list(chain(*temp))
    total2 = list(chain(*arr))
    if total1.count(-1) == total2.count(1):
        res.append(max_v)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
res = []
virus_lst = deque()
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus_lst.append([i, j])

for virus in combi(virus_lst, m):
    bfs(virus)
print(min(res) if res else -1)