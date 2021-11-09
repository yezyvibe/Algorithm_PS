# 중복 불가 : 조합
def c(k,n,m,l):
    if (k == m):
        print(*res)
        return
    else:
        for i in range(n):
            if (visited[i]==0 and arr[i]>l):
                visited[i] = 1
                res[k] = arr[i]
                l = arr[i]
                c(k+1,n,m,l)
                visited[i] = 0

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = [0] * m
visited = [0 for i in range(n)]
c(0,n,m,0)