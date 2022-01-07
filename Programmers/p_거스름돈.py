def solution(n, coins):
    dp = [1] + [0] * n

    for coin in coins:
        for price in range(coin, n+1):
            if price >= coin:
                dp[price] += dp[price - coin]
    return dp[n] % 1000000007

print(solution(5, [1, 2, 5]))