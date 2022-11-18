import sys
import heapq

def dijkstra(start, v):
    hq = [(0, start)]
    INF = float('inf')
    dist = [INF] * (v+1)
    dist[start] = 0

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue

        for next_c, next_n in adj[node]:
            if dist[next_n] > cost + next_c:
                dist[next_n] = cost + next_c
                heapq.heappush(hq, (cost + next_c, next_n))

    return dist    

input = sys.stdin.readline
V, e = map(int, input().split())
k = int(input())
adj = [[] for _ in range(V+1)]
INF = float('inf')

for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))


for i in dijkstra(k, V)[1:]:
    print(i) if i != INF else print('INF')