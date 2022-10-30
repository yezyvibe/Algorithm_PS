from typing import List
from collections import deque

def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[]]
    field = [[[0, [], []] for _ in range(n)] for _ in range(n)]
    # idx - 1
    ices = [[x-1, y-1] for x, y in ices]
    fires = [[x-1, y-1] for x, y in fires]

    # 토템 구분
    for idx, fire in enumerate(fires):
        field[fire[0]][fire[1]][1].append(idx)
    for idx, ice in enumerate(ices):
        field[ice[0]][ice[1]][2].append(idx)

    def is_in(nx, ny):
        if 0 <= nx < n and 0 <= ny < n:
            return True
        return False

    def expand_fires(q):
        dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
        next_q = []
        while q:
            idx, x, y = q.pop()
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if is_in(nx, ny) and idx not in field[nx][ny][1]:
                    field[nx][ny][1].append(idx)
                    next_q.append([idx, nx, ny])
        return next_q

    def expand_ices(q):
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        next_q = []
        while q:
            idx, x, y = q.pop()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if is_in(nx, ny) and idx not in field[nx][ny][2]:
                    field[nx][ny][2].append(idx)
                    next_q.append([idx, nx, ny])
        return next_q

    fires = [[idx, fire[0], fire[1]] for idx, fire in enumerate(fires)]
    ices = [[idx, ice[0], ice[1]] for idx, ice in enumerate(ices)]

    
    # 토템이 맵 전체에 퍼지는 최소 시간
    over_m = 0
    min_m = min(m, n*2)
    if m > n*2:
        over_m = m - n*2

    for _ in range(min_m):
        fires = expand_fires(fires)
        ices = expand_ices(ices)

        for i in range(n):
            for j in range(n):              
                field[i][j][0] += len(field[i][j][1]) - len(field[i][j][2])

    # 나머지 시간은 한꺼번에 더하기
    for i in range(n):
        for j in range(n):
            field[i][j][0] += (len(field[i][j][1]) - len(field[i][j][2])) * over_m

    answer = []
    for i in range(n):
        result = []
        for j in range(n):
            result.append(field[i][j][0])
        answer.append(result)

    return answer

print(solution(
5, 3, [[5, 5], [1, 3], [5, 2]], [[1, 5], [3, 2]]))