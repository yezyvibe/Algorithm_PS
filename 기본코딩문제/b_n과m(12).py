# 조합 # 중복 자연수 존재
def c(k,n,m,l):
    if (k ==m):
        print(*res)
        return
    overlap = 0
    for i in range(n):
        if overlap != arr[i] and arr[i] >= l:
            visited[i] = 1
            overlap = arr[i]
            l = arr[i]
            res[k] = arr[i]
            c(k+1,n,m,l)
            visited[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = [0] * m
visited = [0 for i in range(n)]
c(0,n,m,0)
