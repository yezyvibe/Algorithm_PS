t = int(input())
stack = []

for tc in range(1, t+1):
    n = int(input())
    arr = [list(input().split()) for l in range(n)]
    bg = [[0] * n for m in range(n)]
    bg2 = [[0] * n for m in range(n)]

    for j in range(n):
        for i in range(n-1, -1, -1):
            a = arr[i][j]
            stack.append(a)

    for i in range(n):
        for j in range(n):
            bg[i][j]=arr[n-1-j][i]

    for i in range(n):
        for j in range(n):
            bg2[i][j]=bg[n-1-j][i]

    for i in range(n):
        for j in range(n):
            arr[i][j]=bg2[n-1-j][i]

    print('#{}'.format(tc))
    for i in range(n):
        print('{} {} {}'.format(''.join(bg[i]),''.join(bg2[i]),''.join(arr[i])))