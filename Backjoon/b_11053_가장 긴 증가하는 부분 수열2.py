import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().rstrip().split(' ')))

dp = [0]*n

for i in range(n):
    dp[i] = 1
    for k in range(i):
        if a[i] > a[k]:
            dp[i] = max(dp[k]+1, dp[i])
print(max(dp))