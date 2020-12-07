import sys
import heapq


def dijkstra(n, s, e):
    dist = [INF] * (n + 1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap, [0, s])

    while heap:
        cost, node = heapq.heappop(heap)
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(heap, [c, n])
    return dist[e]


input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
INF = float('inf')
for _ in range(m):
    a, b, c = map(int, input().rstrip().split(' '))
    adj[a].append([b, c])
# print(adj)
s, e = map(int, input().rstrip().split(' '))
print(dijkstra(n, s, e))
