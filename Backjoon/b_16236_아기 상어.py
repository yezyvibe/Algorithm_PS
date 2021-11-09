# 3시 30분-
import sys
from collections import deque


def bfs(q):
    global baby
    global answer

    chk = [[0] * n for _ in range(n)]
    chk[q[0][0]][q[0][1]] = 1
    new_q = deque()
    catch_fish = []
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and bg[nx][ny] <= baby and not chk[nx][ny]:
                new_q.append((nx, ny))  # 갈 수 있는 물고기 위치
                chk[nx][ny] = 1
                if bg[nx][ny] < baby and bg[nx][ny]:  # 먹을 수 있는 물고기
                    catch_fish.append((nx, ny))
    answer += 1
    # for c in chk:
    #     print(c)
    # print()
    check(catch_fish, new_q)


def check(catch_fish, new_q):
    global fish_cnt
    global baby
    if catch_fish:
        if len(catch_fish) == 1:  # 먹을 수 있는 물고기 1마리
            fish_cnt += 1
            bg[catch_fish[0][0]][catch_fish[0][1]] = 0
            catch_fish = deque([(catch_fish[0][0], catch_fish[0][1])])
        else:  # 여러 마리일 때 위치 비교
            catch_fish.sort(key=lambda fish: (fish[0], fish[1]))
            x, y = catch_fish[0][0], catch_fish[0][1]
            bg[x][y] = 0
            catch_fish = deque([(x, y)])
            fish_cnt += 1
        if fish_cnt == baby:  # 먹은 물고기가 자신의 크기와 같을 때 크기 +1
            baby += 1
            fish_cnt = 0
        bfs(catch_fish)  # 먹은 물고기 위치에서 다시 탐색
    for i in range(n):
        for j in range(n):
            if bg[i][j] != 0 and bg[i][j] < baby:
                bfs(new_q)
    else:
        return


input = sys.stdin.readline
n = int(input())
bg = [list(map(int, input().split(' '))) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
baby = 2
q = deque()
fish_cnt = 0
answer = 0
for i in range(n):
    for j in range(n):
        if bg[i][j] == 9:
            q.append((i, j))
            bfs(q)
            break
print(answer, 'answer')
