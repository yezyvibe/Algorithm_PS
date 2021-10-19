import heapq
import sys

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
                heapq.heappush(hq, (dist + 1, node))

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
INF = float('inf')
distance = [INF] * (n+1)
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
dijkstra(x)

answer = []
for i in range(1, n+1):
    if k == distance[i]:
        answer.append(i)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])