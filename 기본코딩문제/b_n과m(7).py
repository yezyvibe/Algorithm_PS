# 중복 가능, 중복 추출 가능
def p(k, n, m):
    if (k == m):
        print(*res)
        return
    else:
        for i in range(n):
            visited[i] = 1
            res[k] = arr[i]
            p(k+1, n, m)
            visited[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = [0] * m
visited = [0 for i in range(n)]
p(0,n,m)