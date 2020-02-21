t = int(input())
for tc in range(1, t+1):
    s = []
    n = int(input())
    for i in range(n):
        c, k = map(str, input().split())
        for j in range(int(k)):
            s.append(c)

    print(f'#{tc}')
    for j in range(len(s)):
        if j % 10 == 0 and j != 0:
            print()
        print(s[j], end='')
    print()