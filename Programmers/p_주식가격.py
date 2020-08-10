def solution(prices):
    result = []
    total = len(prices)
    for i in range(total):
        tmp = prices[i]
        for j in range(i, total):
            next = prices[j]
            if tmp <= next:
                second = j - i
            else:
                second = j - i
                break
        result.append(second)
    return result