import sys
from itertools import combinations as combi
from copy import deepcopy

# dfs 최대!!
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = sys.stdin.readline


def dfs(virus):
    s = []
    for v in virus:
        s.append(v)
    # print(s,'시작')
    while s:
        x, y = s.pop()
        print(x,y, 'xy')
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and chk[nx][ny] == 0:
                print(nx,ny,'11122222222222222222222')
                chk[nx][ny] = 2
                s.append((nx, ny))
    # cnt = 0
    # for i in range(n):
    #     for j in range(m):
    #         if chk[i][j] == 0:
    #             cnt += 1
    # return cnt
    for c in chk:
        print(c)
    return

n, m = map(int, input().split(' '))
bg = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
virus = []
candidates = []
for i in range(n):
    for j in range(m):
        if bg[i][j] == 2:
            virus.append((i, j))
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and bg[nx][ny] == 0:
                    candidates.append((nx, ny))

print(candidates)
print(virus, 'virus')
for c in combi(candidates, 3):
    print(c, 'combi')
    chk = deepcopy(bg)
    for i, j in c:
        chk[i][j] = 1
    else:
        print(dfs(virus))
        # for c in chk:
        #     print(c)