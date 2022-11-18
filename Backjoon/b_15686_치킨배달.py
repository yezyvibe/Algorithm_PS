import sys
from itertools import combinations as combi


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

chickens = []
homes = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] == 1:
            homes.append((i, j))

answer = float('inf')
for c in combi(chickens, m):
    c = list(c)
    total_distance = 0
    
    for a, b in homes:
        min_distance = float('inf')
        for d, e in c:
            min_distance = min((abs(a-d) + abs(b-e)), min_distance)
        total_distance += min_distance
        
        if answer < total_distance:
            break
    else:
        answer = min(total_distance, answer)

print(answer)
