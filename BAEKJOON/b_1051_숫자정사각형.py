n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        for k in range(n if n < m else m): # 행과 열 중 더 작은 것을 기준으로 정사각형 탐색
            if i+k < n and j+k < m: # 주어진 인덱스 벗어나지 않게
                if arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]: # 꼭짓점의 숫자가 모두 같은 지 확인
                    if res < k:
                        res = k
print((res+1)*(res+1))
