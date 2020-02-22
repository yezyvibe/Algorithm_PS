for t in range(1, int(input())+1):
    s = 0
    m = 0
    for n in range(int(input())):
        c = list(map(int,input().split()))

        if c[0] == 0:
            m += s
        elif c[0] == 1:
            s += c[1]
            m += s
        else:
            if c[1] > s:
                c[1] = 0
            else:
                s -= c[1]
                m += s
    print(f'{t} {m}')