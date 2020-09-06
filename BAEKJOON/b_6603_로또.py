def dfs(idx, m, l):
    if (idx == 6):
        print(*res)
        return
    else:
        for i in range(k):
            if visit[i] == 0 and l < num_list[i]:
                visit[i] = 1
                l = num_list[i]
                res[idx] = num_list[i]
                dfs(idx+1, m, l)
                visit[i] = 0
while True:
    num_list = list(map(int, input().split()))
    if len(num_list) == 1 and num_list[0] == 0:
        break
    else:
        k = num_list.pop(0)
        visit = [0]*k
        res = [0]*6
        dfs(0, k, 0)
    print('')
