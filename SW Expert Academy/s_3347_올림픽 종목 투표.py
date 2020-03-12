for t in range(1,int(input())+1):
    n, m = map(int,input().split())
    a_lst = list(map(int,input().split()))
    b_lst = list(map(int,input().split()))
    res = {}
    for b in b_lst:
        for a in a_lst:
            if b >= a:
                idx_a = str(a_lst.index(a))
                if idx_a not in res:
                    res[idx_a] = 1
                    break
                else:
                    res[idx_a] += 1
                    break
    result = 0
    cnt = 0
    for key, val in res.items():
        if cnt < val:
            cnt = val
            result = int(key) + 1
    print('#{} {}'.format(t, result))

