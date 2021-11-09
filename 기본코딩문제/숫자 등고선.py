n = int(input())
x, y = map(int,input().split())
arr = [[0]*n for l in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        while arr[i][j] != 0:
            arr[x][y] = cnt
            cnt += 1
            arr[x-1][y],arr[x+1][y],arr[x][y-1],arr[x][y+1] = cnt

# while문 써서 기준 위치 잡고 그 위치 주변 상하좌우를 +1를 해준다. 그리고 그 다음 값을 기준으로 상하좌우
# 단, 이프문 써서 상하좌우 중 값이 이미 있는 경우에는 패스하기




# 다시 풀기

