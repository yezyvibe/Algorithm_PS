from dis import dis
import sys
import heapq


def dijkstra(start, n, adj, path):
    hq = [[0, start]]
    INF = float('inf')
    dist = [INF] * (n+1)
    dist[start] = 0
    path[start].append(start)
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if dist[cur_node] < cur_cost:
            continue
        for next_cost, next_node in adj[cur_node]:
            tmp_cost = cur_cost + next_cost
            if tmp_cost < dist[next_node]:
                dist[next_node] = tmp_cost
                heapq.heappush(hq, [tmp_cost, next_node])
                path = update_path(path, cur_node, next_node)
    return dist

def update_path(path, cur_node, next_node):
    path[next_node] = []
    for i in path[cur_node]:
        path[next_node].append(i)
    path[next_node].append(next_node)
    return path

input = sys.stdin.readline
n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
path = [[] for _ in range(n+1)]
for i in range(m):
    start_city, end_city, cost = map(int, input().split(" "))
    adj[start_city].append([cost, end_city])
start_city, target_city = map(int, input().split(" "))

dist = dijkstra(start_city, n, adj, path)

print(dist[target_city])
print(len(path[target_city]))
print(' '.join(map(str, path[target_city])))