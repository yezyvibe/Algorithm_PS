import sys
import heapq


def dijkstra(x):
    hq = [(0, x)]
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[x] = 0

    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            new_cost = cost - next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                hq.append((new_cost, next_node))
    return dist

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
INF = float('inf')
for i in range(n-1):
    parent, child, edge = map(int, input().split(" "))
    graph[parent].append((-edge, child))
    graph[child].append((-edge, parent))

max_dist = 0
max_idx = 0
result = dijkstra(1)
for d in range(len(result)):
    if result[d] == INF:
        continue
    if max_dist < result[d]:
        max_dist = result[d]
        max_idx = d
answer = dijkstra(max_idx)[1:]
if n == 1:
    print(0)
else:
    print(max(answer))