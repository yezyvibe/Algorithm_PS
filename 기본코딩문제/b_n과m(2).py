# 조합 (중복 불가)
def c(k,n,m,l):
    if (k==m):
        print(*res)
        return
    else:
        for i in range(n):
            if (visited[i]==0 and l <arr[i]):
                visited[i] = 1
                l = arr[i]
                res[k] = arr[i]
                c(k+1,n,m,l)
                visited[i] = 0

n, m = map(int, input().split())
arr = range(1, n+1)
visited = [0 for i in range(n)]
res = [0] * m
c(0,n,m,0)