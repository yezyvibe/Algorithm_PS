import sys
import heapq

def dijkstra(s):
    hq = [(0, s)]
    answer = 0

    visit = [0] * (v+1)
    cnt = 0 
    while hq:

        if cnt == v:
            break

        cost, node = heapq.heappop(hq)
        if not visit[node]:
            visit[node] = 1
            answer += cost
            cnt += 1

            for n_cost, n_node in adj[node]:
                heapq.heappush(hq, (n_cost, n_node))

    return answer

input = sys.stdin.readline
v, e = map(int, input().split())
adj = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

print(dijkstra(1))