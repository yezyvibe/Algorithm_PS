import sys
import heapq


def dijkstra(start, n, adj):
    hq = [(0, start)]
    inf = float('inf')
    dist = [inf] * (n+1)
    dist[start] = 0

    while hq:
        cost, node = heapq.heappop(hq)

        for next_cost, next_node in adj[node]:
            
            if dist[next_node] > dist[node] + next_cost:
                dist[next_node] = dist[node] + next_cost
                heapq.heappush(hq, (cost+next_cost, next_node))
    
    return dist


input = sys.stdin.readline
n, m, k, x = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append((1, b))


result = dijkstra(x, n, adj)
if k in result:
    for i in range(1, len(result)):
        if result[i] == k:
            print(i)
else:
    print(-1)

# 도시의 개수 n -> 300,000 까지니까 완전탐색 불가능

