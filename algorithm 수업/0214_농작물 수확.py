t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for l in range(n)]
    result = 0

    for i in range(n):
        for j in range(n):
            if abs(i-(n//2)) + abs(j-(n//2)) <= (n//2):
                result += arr[i][j]

    print('#{} {}'.format(tc,result))