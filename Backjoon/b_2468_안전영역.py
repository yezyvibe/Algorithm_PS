import sys

def dfs(arr, i, j):
    stack = [(i, j)]
    arr[i][j] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    n = len(arr)

    while stack:
        x, y = stack.pop()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if not arr[nx][ny]:
                    stack.append((nx, ny))
                    arr[nx][ny] = 1
    return arr

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0

max_height = max(map(max, arr))

for h in range(0, max_height + 1):
    check = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] <= h:
                check[i][j] = 1  # 잠긴 영역 1로 표시

    cnt = 0
    for i in range(n):
        for j in range(n):
            if not check[i][j]: # 잠기지 않으니까 탐색 시작
                check = dfs(check, i, j)
                cnt += 1

    answer = max(cnt, answer)

print(answer)