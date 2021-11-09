T = int(input())

for t in range(1,T+1):
    N = int(input())
    mul = [2, 3, 5, 7, 11]
    j = 0
    cnt = 0
    res = []
    while cnt != 5:
        if N % mul[cnt] == 0:
            j += 1
            N = N//mul[cnt]
        else:
            res.append(j)
            j = 0
            cnt += 1
    print('#{} {}'.format(t, ' '.join(map(str, res))))