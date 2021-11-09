# 조합 #N개 중 동일한 자연수 있음
def c(k,n,m,l):
    if (k==m):
        print(*res)
        return

    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != arr[i] and arr[i] >= l:
            visited[i] = 1
            res[k] = arr[i]
            l = arr[i]
            overlap = arr[i]
            c(k+1, n, m, l)
            visited[i] = 0

n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
res = [0] * m
visited = [0 for i in range(n)]
c(0,n,m,0)
