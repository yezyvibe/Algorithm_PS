dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(i, j):
    s = [(i, j)]
    bg[i][j] = 2
    while s:
        x, y = s.pop()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(bg) and 0 <= ny < len(bg[0]):
                if bg[nx][ny] == 1:
                    s.append((nx, ny))
                    bg[nx][ny] = 2


while True:
    w, h = map(int, input().split(' '))
    if w == h == 0:
        break
    bg = [list(map(int, input().split(' '))) for _ in range(h)]
    cnt = 0
    for i in range(len(bg)):
        for j in range(len(bg[0])):
            if bg[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)
