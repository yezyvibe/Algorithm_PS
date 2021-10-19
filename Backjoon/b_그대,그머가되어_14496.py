import sys
import heapq


def dijkstra(start):
    hq = [(0, start)]
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for node in adj[now]:
            if distance[node] > dist + 1:
                distance[node] = dist + 1
                hq.append((dist+1, node))
    

    
input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())
INF = float('inf')
distance = [INF] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

dijkstra(a)
if distance[b] == INF:
    print(-1)
else:
    print(distance[b])