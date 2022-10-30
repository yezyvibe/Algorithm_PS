
from typing import List

def solution(wall: List[str]) -> List[List[int]]:
    n, m = len(wall), len(wall[0])
    INF = float('inf')

    def dfs(a, b):
        INF = float('inf')
        visit = [[INF]*m for _ in range(n)]
        visit[a][b] = 1
        stack = [(a, b)]
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        while stack:
            x, y = stack.pop()
            # 1번
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if wall[nx][ny] == 'H':
                        # 상하좌우 중 홀드인 경우
                        if (visit[nx][ny] != INF and visit[nx][ny] > visit[x][y] + 1) or visit[nx][ny] == INF:
                            visit[nx][ny] = visit[x][y]+1
                            stack.append((nx, ny))

            # 2번
            # 좌로 2칸 떨어진 게 홀드이면
            if 0 <= y - 2 < m and wall[x][y-2] == 'H':
                for j in range(y-2, y+1):
                    if wall[x-1][j] != '.':
                        break
                else:
                    if wall[x][y-1] == '.':
                        # visit[x][y-2] = min(visit[x][y-2], visit[x][y]+1)
                        # stack.append((x, y-2))
                        if (visit[x][y-2] != INF and visit[x][y-2] > visit[x][y] + 1) or visit[x][y-2] == INF:
                            visit[x][y-2] = visit[x][y]+1
                            stack.append((x, y-2))
            # 좌로 3칸
            if 0 <= y - 3 < m and wall[x][y-3] == 'H':
                for j in range(y-3, y+1):
                    if wall[x-1][j] != '.':
                        break
                else:
                    for l in range(y-2, y):
                        if wall[x][l] != '.':
                            break
                    else:
                        # visit[x][y-3] = min(visit[x][y-3], visit[x][y]+1)
                        # stack.append((x, y-3))
                        if (visit[x][y-3] != INF and visit[x][y-3] > visit[x][y] + 1) or visit[x][y-3] == INF:
                            visit[x][y-3] = visit[x][y]+1
                            stack.append((x, y-3))

            # 우로 2칸
            if 0 <= y + 2 < m and wall[x][y+2] == 'H':
                for j in range(y, y+3):
                    if wall[x-1][j] != '.':
                        break
                else:
                    if wall[x][y+1] == '.':
                        # visit[x][y-2] = min(visit[x][y-2], visit[x][y]+1)
                        # stack.append((x, y-2))
                        if (visit[x][y+2] != INF and visit[x][y+2] > visit[x][y] + 1) or visit[x][y+2] == INF:
                            visit[x][y+2] = visit[x][y]+1
                            stack.append((x, y+2))
            # 좌로 3칸
            if 0 <= y + 3 < m and wall[x][y+3] == 'H':
                for j in range(y, y+4):
                    if wall[x-1][j] != '.':
                        break
                else:
                    for l in range(y+1, y+3):
                        if wall[x][l] != '.':
                            break
                    else:
                        # visit[x][y-3] = min(visit[x][y-3], visit[x][y]+1)
                        # stack.append((x, y-3))
                        if (visit[x][y+3] != INF and visit[x][y+3] > visit[x][y] + 1) or visit[x][y+3] == INF:
                            visit[x][y+3] = visit[x][y]+1
                            stack.append((x, y+3))
        
            # 3번
            if 0 <= x-2 < n and wall[x-1][y] == '.' and wall[x-2][y] == 'H':
                if (visit[x-2][y] != INF and visit[x-2][y] > visit[x][y] + 1) or visit[x-2][y] == INF:
                    visit[x-2][y] = visit[x][y]+1
                    stack.append((x-2, y))
            # 4번
            if 0<= x-1< n and  0 <= y-1 < m and wall[x-1][y-1] == 'H':
                if wall[x][y-1] == '.' and wall[x-1][y] == '.':
                    # visit[x-1][y-1] = min(visit[x-1][y-1], visit[x][y]+1)
                    # stack.append((x-1, y-1))
                    if (visit[x-1][y-1] != INF and visit[x-1][y-1] > visit[x][y] + 1) or visit[x-1][y-1] == INF:
                        visit[x-1][y-1] = visit[x][y]+1
                        stack.append((x-1, y-1))
            # 5번
            if 0<= x-1 < n and  0 <= y+1 < m and wall[x-1][y+1] == 'H':
                if wall[x][y+1] == '.' and wall[x-1][y] == '.':
                    # visit[x+1][y+1] = min(visit[x+1][y+1], visit[x][y]+1)
                    # stack.append((x+1, y+1))
                    if (visit[x-1][y+1] != INF and visit[x-1][y+1] > visit[x][y] + 1) or visit[x-1][y+1] == INF:
                        visit[x-1][y+1] = visit[x][y]+1
                        stack.append((x-1, y+1))
        
        return visit

    answer = [[-1] * m for _ in range(n)]
    result = dfs(n-1, 0)
    for i in range(n):
        for j in range(m):
            if result[i][j] != INF:
                answer[i][j] = result[i][j]
            else:
                if wall[i][j] == '.' or wall[i][j] == 'X':
                    answer[i][j] = 0
    return answer


wall = ["....HH", "H..H.H"]
print(solution(wall))