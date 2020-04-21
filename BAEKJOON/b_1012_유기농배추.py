for tc in range(1,int(input())+1):
    m, n, k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    stack = []
    cnt = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(k):
        y, x = map(int,input().split())
        arr[x][y] = 1

    for i in range(m):
        for j in range(n):
            if arr[j][i] == 1:
                stack.append((j,i))
                # arr[j][i] = 2
                while stack:
                    # print(stack)
                    x, y = stack.pop()
                    arr[x][y] = 2
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<= nx < n and 0<= ny < m:
                            if arr[nx][ny]== 1:
                                stack.append((nx, ny))
                                # arr[nx][ny] = 2
                cnt += 1
    print(cnt)


