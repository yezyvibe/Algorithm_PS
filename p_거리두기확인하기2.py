def dfs(i, j, place):
    s = [(i, j)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while s:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if abs(i-nx) + abs(j-ny) <= 2:
                    if place[nx][ny] == 'P':
                        return False
                    elif place[nx][ny] == 'O':
                        s.append((nx, ny))
        place[x][y] = '#'
    return True


def solution(places):
    answer = []
    for place in places:
        chk = 0
        place = [list(p) for p in place]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    res = dfs(i, j, place)
                    if not res:
                        answer.append(0)
                        chk = 1
                        break
            if chk:
                break
        else:
            answer.append(1)
    return answer