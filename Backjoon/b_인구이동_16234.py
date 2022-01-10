from collections import deque
import sys
import math 


def search(i, j, border):
    global is_union
    q = deque([(i, j)])
    border[i][j] = 1
    total_population = arr[i][j]
    visit = [(i, j)]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not border[nx][ny]:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    border[nx][ny] = 1
                    total_population += arr[nx][ny]
                    visit.append((nx, ny))
                    q.append((nx, ny))

    if len(visit) > 1:
        is_union = True
        union = math.floor(total_population / len(visit))
        for x, y in visit:
            arr[x][y] = union


input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
while True:
    is_union = False
    border = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not border[i][j]:
                search(i, j, border)
    if is_union:
        answer += 1
    else:
        break
print(answer)