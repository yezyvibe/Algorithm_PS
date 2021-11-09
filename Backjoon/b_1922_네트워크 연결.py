import heapq

def prim(v):
    q = []
    mst[v] = 1
    result = 0
    for i in adj[v]:
        heapq.heappush(q, i)
    while q:
        c, v = heapq.heappop(q)
        if not mst[v]:
            mst[v] = 1
            result += c
            for j in adj[v]:
                heapq.heappush(q, j)
        if sum(mst) == n:
            return result

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
mst = [0]*(n+1)
i = 0
while i < m:
    a, b, c = map(int, input().split())
    adj[a].append([c,b])
    adj[b].append([c,a])
    i += 1
print(prim(1))