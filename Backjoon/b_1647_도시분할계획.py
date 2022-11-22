import sys
from heapq import heappop, heappush

def prim(s):
    hq = [(0, s)]
    answer = 0
    max_cost = 0
    visit = [0] * (n+1)
    cnt = 0

    while hq:

        if cnt == n:
            break

        cost, node = heappop(hq)

        if not visit[node]:
            visit[node] = 1
            answer += cost
            cnt += 1
            max_cost = max(max_cost, cost)
            for n_cost, n_node in adj[node]:
                if not visit[n_node]:
                    heappush(hq, (n_cost, n_node))
                    
    return answer - max_cost



input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

print(prim(1))