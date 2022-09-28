import heapq

def dijkstra(start, end, adj, n):
    hq = [(0, start)]
    dist = [float('inf')]*(n+1)
    dist[start] = 0
    visit = [0]*(n+1)
    visit[start] = 1
    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        for next_cost, next_node in adj[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

    return dist[end]


def solution(num, s, a, b, fares):
    adj = [[] for _ in range(num+1)]
    for i in range(len(fares)):
        x, y, cost = fares[i]
        adj[x].append((cost, y))
        adj[y].append((cost, x))
    
    answer = float('inf')
    for i in range(1, num+1):
        together = dijkstra(i, s, adj, num)
        muzi = dijkstra(i, a, adj, num)
        appeach =dijkstra(i, b, adj, num)
        res = together + muzi + appeach
        if answer > res:
            answer = res
    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))