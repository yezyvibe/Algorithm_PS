import sys
import heapq


def dijkstra(start, end):
    hq = [(0, start)]
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[start] = 0

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue

        for next_c, next_n in adj[node]:
            new_cost = cost + next_c

            if dist[next_n] > new_cost:
                dist[next_n] = new_cost
                heapq.heappush(hq, (new_cost, next_n))
    
    return dist[end]


input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

start, end = map(int, input().split())

print(dijkstra(start, end))