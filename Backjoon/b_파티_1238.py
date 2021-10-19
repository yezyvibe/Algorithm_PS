import heapq
import sys


def dijkstra(start, end):
    distance = [INF] * (n+1)
    hq = [(0, start)]
    distance[start] = 0
    while hq:
        dist, now = heapq.heappop(hq)
        if distance[now] < dist:
            continue
        for cost, node in adj[now]:
            if distance[node] > cost + dist:
                distance[node] = cost + dist
                heapq.heappush(hq, (cost + dist, node))
    return distance[end]



input = sys.stdin.readline
n, m, x = map(int, input().split())
adj = [[] for _ in range(n+1)]
INF = float('inf')
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))

answer = 0
for i in range(1, n+1):
    result = dijkstra(i, x) + dijkstra(x, i)
    if answer < result:
        answer = result
print(answer)