# 순열, 중복추출 불가
def p(k, n, m):
    if(k==m):
        print(*res)
        return

    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != arr[i]:
            visited[i] = 1
            res[k] = arr[i]
            overlap = arr[i]
            p(k+1, n, m)
            # 재귀 끝나고 초기화
            visited[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int, input().split())))
res = [0] * m
visited = [0 for i in range(n)]
p(0, n, m)