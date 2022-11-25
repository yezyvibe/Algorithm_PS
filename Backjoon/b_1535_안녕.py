import sys


input = sys.stdin.readline
n = int(input())
strength = [0] + list(map(int, input().split()))
pleasure = [0] + list(map(int, input().split()))

# 배낭 문제 (가방이 체력, 가치가 기쁨)
dp = [[0] * (101) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        if strength[i] > j: # 담을 수 없는 경우
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(pleasure[i] + dp[i-1][j - strength[i]], dp[i-1][j])

print(dp[n][99])