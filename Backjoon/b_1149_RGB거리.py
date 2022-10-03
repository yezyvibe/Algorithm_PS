import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# dp 배열 먼저 만들기
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[i][0] = arr[i][0]
        dp[i][1] = arr[i][1]
        dp[i][2] = arr[i][2]
        continue
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]
print(min(dp[-1]))