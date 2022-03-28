def solution(money, costs):
    coins = [1, 5, 10, 50, 100, 500]
    
    values = []

    for i in range(len(costs)):
        value = coins[i] / costs[i]
        values.append((value, coins[i], costs[i]))
    
    values.sort()
    answer = 0
    while money > 0:
        val, coin, cost = values.pop()
        q, r = divmod(money, coin)
        answer += q * cost
        money = r
    return answer
    
print(solution(4578,[1, 4, 99, 35, 50, 1000] ))