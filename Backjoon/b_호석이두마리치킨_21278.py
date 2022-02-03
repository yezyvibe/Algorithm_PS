import sys

input = sys.stdin.readline
n, m = map(int, input().split())
INF = float('inf')
cost = [[INF] * n for _ in range(n)] 

for _ in range(m):
    a, b = map(int, input().split())
    cost[a-1][b-1] = 1
    cost[b-1][a-1] = 1

for k in range(n):
    cost[k][k] = 0
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])   # i->j로 직행이 빠른지 다른 곳을 거쳐서 가는게 빠른지 확인

min_v = INF
answer = []
for i in range(n-1):
    for j in range(i+1, n):
        sum = 0
        for k in range(n):
            sum += min(cost[k][i], cost[k][j])
        if min_v > sum * 2:
            min_v = sum * 2 
            answer = [i+1, j+1, min_v]
print(*answer)