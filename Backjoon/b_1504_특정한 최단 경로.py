# 다익스트라
import sys
import heapq


def dijkstra(s):
    dist = [INF] * (N + 1)
    dist[s] = 0
    heap = []
    heapq.heappush(heap, [0, s])

    while heap:
        cost, node = heapq.heappop(heap)
        if dist[node] < cost:
            continue
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(heap, [c, n])
    return dist


input = sys.stdin.readline
N, E = map(int, input().split(' '))
adj = [[] for _ in range(N + 1)]
INF = float('inf')
for _ in range(E):
    a, b, c = map(int, input().split(' '))
    adj[a].append((b, c))
    adj[b].append((a, c))
v1, v2 = map(int, input().split(' '))
s_d = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)

# 케이스 두 개 중 최솟값 -> 시작,v1, v2, 끝 / 시작,v2, v1, 끝
res = min(s_d[v1] + v1_d[v2] + v2_d[N], s_d[v2] + v2_d[v1] + v1_d[N])
print(res if res < INF else -1)