import sys
import heapq


def dijkstra(start):
    hq = [(0, start)]
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for cost, node in adj[now]:
            if distance[node] > cost + dist:
                distance[node] = cost + dist
                heapq.heappush(hq, (cost+dist, node))

input = sys.stdin.readline
n, m, c = map(int, input().split())
INF = float('inf')
distance = [INF] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())  
    adj[x].append((z, y))
dijkstra(c)
print(distance)

cnt = 0
max_v = 0
for i in range(1, n+1):
    if i != INF:
        cnt += 1
        max_v = max(max_v, distance[i])
print(cnt-1, max_v)