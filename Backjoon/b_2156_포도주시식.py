import sys
input = sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0]*(n+1)
# 첫 번째
dp[1] = wine[0]
# 두 번째
if n > 1:
    dp[2] = dp[1] + wine[1]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3]+wine[i-2]+wine[i-1], dp[i-2]+wine[i-1])

print(dp[n])