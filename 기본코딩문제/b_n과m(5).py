# 순열
def p(k,n,m):
    if (k == m):
        print(*res)
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                res[k] = n_lst[i]
                p(k+1, n, m)
                visited[i] = 0

n, m = map(int,input().split())
n_lst = sorted(list(map(int, input().split())))
res = [0] * m
visited = [0 for i in range(n)]

p(0,n,m)
