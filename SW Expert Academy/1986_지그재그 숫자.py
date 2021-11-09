t = int(input())
for tc in range(1,t+1):
    n = int(input())
    res = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            res += i
        else:
            res -= i
    print('#{} {}'.format(tc, res))