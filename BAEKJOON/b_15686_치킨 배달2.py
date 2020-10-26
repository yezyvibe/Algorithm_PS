import sys
from itertools import combinations as combi

input = sys.stdin.readline

n, m = map(int, input().split(' '))
bg = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if bg[i][j] == 1:
            house.append((i, j))
        elif bg[i][j] == 2:
            chicken.append((i, j))

chicken_com = list(combi(chicken, m))
min_v = 1000000
for com in chicken_com:
    chk = [[0] * n for _ in range(n)]
    for item in com:  # 한 세트
        for h in house:
            distance = abs(item[0] - h[0]) + abs(item[1] - h[1])
            if not chk[h[0]][h[1]]:
                chk[h[0]][h[1]] = distance
            else:
                if distance < chk[h[0]][h[1]]:
                    chk[h[0]][h[1]] = distance
    res = 0
    for h in house:
        res += chk[h[0]][h[1]]
    if res < min_v:
        min_v = res
print(min_v)

# 두 번째 풀이 시간 1/2
# min_v = float('INF')
# for chi in combi(chicken, m):
#     sum_v = 0
#     for h in house:
#         sum_v += min([abs(h[0]-c[0]) + abs(h[1]-c[1]) for c in chi])
#         if min_v <= sum_v:
#             break
#     else:
#         if sum_v < min_v:
#             min_v = sum_v
# print(min_v)
