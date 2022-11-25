import sys


input = sys.stdin.readline
N, K = map(int, input().split())
weights = [0] * (N + 1)
values= [0] * (N + 1)
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    W, V = map(int, input().split())
    weights[i+1] = W
    values[i+1] = V


for i in range(1, N+1):
    for j in range(1, K+1):
        
        if weights[i] > j:
            dp[i][j] = dp[i-1][j]
        
        else:
            dp[i][j] = max(values[i] + dp[i-1][j - weights[i]], dp[i-1][j])

print(max(map(max, dp)))

