def dfs(cur, cnt):
    global result

    if (max_v == result):
        if (n-cnt) % 2 == 0:
            return

    if (cnt == n):
        result = max(result, int(''.join(num)))
        return

    for i in range(0, len(num)-1):
        for j in range(i+1, len(num)):
            if (num[i] < num[j]):
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
                tmp_num = int(''.join(num))
                if tmp_num not in dist[cnt]:
                    dfs(i, cnt+1)
                    dist[cnt].append(tmp_num)
                    tmp = num[i]
                    num[i] = num[j]
                    num[j] = tmp

for tc in range(1, int(input())+1):
    num, n = input().split()
    num = list(num)
    n = int(n)
    max_v = int(''.join(sorted(num, reverse=True)))
    dist = {i: [] for i in range(n+1)}
    result = 0
    dfs(0, 0)
    print('#{} {}'.format(tc, result))
