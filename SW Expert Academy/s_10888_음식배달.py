from itertools import combinations as combi


def distance(combi_lst, house):
    sum = 0
    for x, y in house:
        min_v = 10000000
        for a in combi_lst:
            for b in a:
                tmp = abs(x - b[0]) + abs(x - b[1])
                if tmp < min_v:
                    min_v = tmp
        sum += min_v
    for a in combi_lst:
        for b in a:
            sum += bg[b[0]][b[1]]
    return sum


for tc in range(1, int(input()) + 1):
    n = int(input())
    bg = [list(map(int, input().split())) for _ in range(n)]
    house = []
    chicken = []
    for i in range(n):
        for j in range(n):
            if bg[i][j] == 1:
                house.append([i, j])
            elif bg[i][j] >= 2:
                chicken.append([i, j])

    if len(chicken) == 1:
        cx, cy = chicken[0][0], chicken[0][1]
        sum = bg[cx][cy]
        for x, y in house:
            dx = abs(cx - x)
            dy = abs(cy - y)
            sum += (dx + dy)
        answer = sum


    else:
        answer = 10000000
        for i in range(2, len(chicken) + 1):
            combi_lst = list(combi(chicken, i))
            res = distance(combi_lst, house)
            if res < answer:
                answer = res

    print('#{} {}'.format(tc, answer))
