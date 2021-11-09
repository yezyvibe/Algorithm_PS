# 순열로
# 같은 수 여러번 뽑기 가능
def p(k,n,m):
    if (k == m):
        print(*res)
        return
    else:
        for i in range(n):
            visited[i] = 1
            res[k] = arr[i]
            p(k+1,n,m)
            visited[i] = 0

n, m = map(int,input().split())
arr = range(1, n+1)
res = [0] * m
visited = [ 0 for i in range(n)]
p(0,n,m)