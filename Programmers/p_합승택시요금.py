# import heapq

# def solution(n, s, a, b, fares):
#     d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
#     for x in range(n):
#         d[x][x] = 0
#     for x, y, c in fares:
#         d[x-1][y-1] = c
#         d[y-1][x-1] = c

#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 if d[j][k] > d[j][i] + d[i][k]:
#                     d[j][k] = d[j][i] + d[i][k]

#     minv = 40000002
#     for i in range(n):
#         minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
#     return minv

import heapq

def dijkstra(start, adj, dist):
    hq = [(0, start)]
    dist[start] = 0

    while hq:
        cost, current = heapq.heappop(hq)
        for next, fare in adj[current]:
            if dist[next] > cost + fare:
                dist[next] = cost + fare
                heapq.heappush(hq, (cost+fare, next))
    


def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n+1)]
    INF = float('inf')
    dist_a = [INF] * (n+1)
    dist_b = [INF] * (n+1)
    dist_s = [INF] * (n+1)
    for x, y, fare in fares:
        adj[x].append((y, fare))
        adj[y].append((x, fare))

    dijkstra(a, adj, dist_a)
    dijkstra(b, adj, dist_b)
    dijkstra(s, adj, dist_s)
    
    min_v = INF
    for i in range(1, n+1):
        total = dist_a[i] + dist_b[i] + dist_s[i]
        min_v = min(min_v, total)        
    return min_v


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))