t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for l in range(100)]
    result1=0
    result2=0
#가로
    for m in range(100):
        for i in range(100):
            for j in range(100):
                if j+m <= 100:
                    b = arr[i][j:j+m]
                    if b == b[::-1]:
                        result1=m
#세로
    for i in range(100):
        for j in range(i,100):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for m in range(100):
        for i in range(100):
            for j in range(100):
                if j+m <= 100:
                    b = arr[i][j:j+m]
                    if b == b[::-1]:
                        result2=m
    print('#{} {}'.format(tc,max(result1,result2)))