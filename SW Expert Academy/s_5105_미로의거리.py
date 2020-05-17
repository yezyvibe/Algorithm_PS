# 최단경로찾기
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    q = []
    result = 0

    # 시작점 잡기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                q.append((i, j))
                arr[i][j] = 0
                break
    while q:
        x, y = q.pop(0)
        cnt = arr[x][y] + 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    arr[nx][ny] = cnt
                    arr[x][y] = 1
                elif arr[nx][ny] == 3:
                    result = cnt - 1
                    break
    print('#{} {}'.format(tc, result))