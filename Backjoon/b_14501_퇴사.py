import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]

dp = [0] * n

for i in range(n):
    if i + arr[i][0] <= n:
        dp[i] = arr[i][1]
        for k in range(i):
            if k + arr[k][0] <= i:
                dp[i] = max(dp[i], arr[i][1] + dp[k])
print(max(dp))
