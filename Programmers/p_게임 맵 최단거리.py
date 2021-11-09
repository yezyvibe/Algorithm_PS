from collections import deque

def solution(maps):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque([(0, 0)])

    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    visit[0][0] = 1
    maps[0][0] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < len(maps) and 0<= ny < len(maps[0]):
                if maps[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    
        
    answer = -1
    if visit[-1][-1]:
        return visit[-1][-1]
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))