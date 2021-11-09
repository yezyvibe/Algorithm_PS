# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs():
    stack = []
    x, y = 1, 1
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        if arr[x][y] == 3:
            return 1

        arr[x][y] = 1
        for i in range(len(dx)):
            if arr[x+dx[i]][y+dy[i]] == 0:
                stack.append((x+dx[i], y+dx[i]))
    return 0

for tc in range(1, 11):
    input()
    arr = [list(input()) for l in range(16)]
    print('#{} {}'.format(tc, dfs()))
