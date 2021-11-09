t = int(input())

for tc in range(1,t+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = [0, 0, 0, 0, 0, 0, 0, 0]
    n = int(input())

    for i in money:
        s = n // i
        n = n % i
        idx = money.index(i)
        res[idx] = s
    print(f'#{tc}')
    print(' '.join(map(str,res)))