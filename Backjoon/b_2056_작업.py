import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
graph = [[] for _ in range(n+1)]
answer = 0
for i in range(1, n+1):
    cost, cnt, *lst = map(int, input().split())
    dp[i] = cost
    for x in lst:
        graph[i].append(x) # i를 풀기 전 풀어야 한 선행 문제들 저장

for i in range(1, n+1):
    max_cost = 0
    for j in graph[i]:
        max_cost = max(dp[j], max_cost)
    dp[i] += max_cost
    answer = max(dp[i], answer)
    
print(max(dp))