for t in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    r = 0
    c = n // 2
    res = arr[r][c] + arr[n-1][c]
    for i in range(1, c):
        r += 1
        for j in range(c-i, c+i+1):
            res += arr[r][j]
            res += arr[r+2*(c-i)][j]
    for k in range(n):
        res += arr[c][k]
    if n == 1:
        res = arr[0][0]
    print('#{} {}'.format(t, res))