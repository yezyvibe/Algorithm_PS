n = int(input())
p = list(map(int, input().split(' ')))
dp = [0]*n
dp[0] = p[0]
dp[1] = max(p[1], dp[0]*2)

for i in range(2, n):
    dp[i] = p[i]
    for j in range(i//2+1):
        dp[i] = max(dp[i], dp[j]+dp[i-j-1])
print(dp[n-1])