for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    cheeze = list(map(int, input().split()))
    pizza_num = [(i+1, cheeze[i]) for i in range(m)]
    baking = pizza_num[:n]

    while baking:
        num, c = baking.pop(0)
        old = c // 2

        if old == 0:
            if n == m:
                continue
            else:
                num, c = pizza_num[n]
                n += 1
                baking.append((num, c))
        else:
            baking.append((num, old))

    print('#{} {}'.format(tc, num))