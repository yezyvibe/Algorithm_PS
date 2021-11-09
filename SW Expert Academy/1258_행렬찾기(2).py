#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for t in range(1, int(input())+1):
    res = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                #시작점
                x = i
                y = j
                #최대 행열의 크기
                max_r = 0
                max_c = 0
                #열 크기
                while 0 <= y <n and arr[x][y] != 0:
                    y = y + dy[3]
                max_c = y - 1

                #행 크기
                while 0 <= x < n and arr[x][y-1] != 0:
                    x = x + dx[1]
                max_r = x-1

                for k in range(i, max_r+1):
                    for m in range(j, max_c+1):
                        arr[k][m] = 0
                res.append((max_r-i+1, max_c-j+1))
    matrix = []
    for r, c in res:
        matrix.append([r*c,r,c])
    matrix.sort()

    print(f'#{t} {len(matrix)}', end=' ')
    for i in range(len(matrix)):
        print(matrix[i][1], matrix[i][2],end=' ')
    print()