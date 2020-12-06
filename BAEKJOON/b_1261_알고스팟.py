import sys
import heapq


def dijkstra():
    heap = []
    heapq.heappush(heap, [0, 0, 0])  # 시작점
    visit[0][0] = 1

    while heap:
        cnt, x, y = heapq.heappop(heap)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if x == n - 1 and y == m - 1:  # 종료조건
                print(cnt)
                break
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                visit[nx][ny] = 1

                if maze[nx][ny]:
                    heapq.heappush(heap, [cnt + 1, nx, ny])
                else:
                    heapq.heappush(heap, [cnt, nx, ny])


input = sys.stdin.readline
m, n = map(int, input().rstrip().split(' '))
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# print(visit)
# print(m, n, maze)
dijkstra()
# print(visit[n-1][m-1])
