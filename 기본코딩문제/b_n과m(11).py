# 순열 #겹치는 자연수 있음
def p(k,n,m):
    if (k==m):
        print(*res)
        return
    overlap = 0
    for i in range(n):
        if overlap != arr[i]:
            visited[i] = True
            overlap = arr[i]
            res[k] = arr[i]
            p(k+1,n,m)
            visited[i] = False

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = [0] * m
visited = [0 for i in range(n)]
p(0,n,m)