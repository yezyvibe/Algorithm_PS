# 순열하고 조합 만들기 기초
# 여기서는 순열 (중복 가능)
def p(k,n,m):
    if (k == m):
        print(*res)
        return
    else:
        for i in range(n):
            if(visited[i] == 0):
                visited[i] = 1
                res[k] = arr[i]
                p(k+1, n, m)
                visited[i] = 0

n, m = map(int,input().split())
arr = range(1, n+1)
res = [0] * m
visited = [0 for i in range(n)]

p(0,n,m)