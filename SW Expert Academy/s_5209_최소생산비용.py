def dfs_cost(product):
    global cost, res
    if product == n:
        res = min(res, cost)
        return
    if cost > res:
        return

    for i in range(n):
        if not factory[i]:
            factory[i] = 1
            cost += arr[product][i]
            dfs_cost(product+1)
            cost -= arr[product][i]
            factory[i] = 0
    return

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    factory = [0]*n
    cost = 0
    res = 1000000000000

    dfs_cost(0)
    print('#{} {}'.format(tc, res))