import heapq
import sys

input = sys.stdin.readline


def dijkstra(v, s, adj):
    dist = [INF] * (v + 1)  # 최단경로 리스트
    dist[s] = 0
    heap = []
    heapq.heappush(heap, [0, s])

    while heap:
        cost, node = heapq.heappop(heap)  # 최소힙 이용
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(heap, [c, n])
    return dist


V, E = map(int, input().split())
s = int(input())
adj = [[] for _ in range(V + 1)]
INF = float('inf')  # 초기값은 무한대
for i in range(E):  # 인접리스트
    u, v, w = map(int, input().split())
    adj[u].append([v, w])

for res in dijkstra(V, s, adj)[1:]:
    print(res if res != INF else 'INF')
