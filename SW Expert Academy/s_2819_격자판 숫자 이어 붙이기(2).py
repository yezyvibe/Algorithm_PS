for t in range(1,int(input())+1):
    #배열에서 int가 아닌 str 형태로 입력받기
    arr = [input().split() for _ in range(4)]
    result = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        for j in range(4):
            stack = [(i,j,0,arr[i][j])]
            while stack:
                x, y, cnt, num = stack.pop()
                if cnt == 6:
                    result.add(num)
                else:
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<= nx < 4 and 0<= ny < 4:
                            stack.append((nx,ny,cnt+1,arr[nx][ny]+num))
    print('#{} {}'.format(t,len(result)))



