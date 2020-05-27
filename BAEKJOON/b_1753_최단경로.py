import heapq
import sys
input = sys.stdin.readline

def dijkstra(v, k, adj):
    q = []
    dist = [INF]*(v+1)
    dist[k] = 0
    heapq.heappush(q, [0, k])

    while q:
        cost, node = heapq.heappop(q)
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(q, [c, n])
    return dist

V, E = map(int, input().split())
k = int(input())
adj = [[] for _ in range(V+1)]
INF = float('inf')
for i in range(E):
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

for i in list(dijkstra(V, k, adj))[1::]:
    print(i if i != float('inf') else 'INF')
