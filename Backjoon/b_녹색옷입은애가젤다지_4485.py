import sys
import heapq


def dijkstra():
    hq = [(arr[0][0], 0, 0)]
    distance[0][0] = arr[0][0]

    while hq:
        dist, x, y = heapq.heappop(hq)
        if distance[x][y] < dist:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + arr[nx][ny]
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(hq, (cost, nx, ny))
    return distance[n-1][n-1]

input = sys.stdin.readline
INF = float('inf')
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    distance = [[INF]*n for _ in range(n)]
    answer = dijkstra()
    print(f'Problem {cnt}: {answer}')
    cnt += 1