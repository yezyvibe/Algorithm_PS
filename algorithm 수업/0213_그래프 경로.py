t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[0]*v for l in range(v)]
    temp = []
    start, end = map(int,input().split())
    b = 0
    temp.append(start-1)

# 배열 만들기
    for n in range(e):
        i, j = map(int, input().split())
        arr[i-1][j-1] = 1

    while True:
        if b == -1:
            break
        if len(temp) == 0:
            result = 0
            break

        s = temp.pop()
        for j in range(len(arr[s])):
            if arr[s][j] == 1:
                if j == end-1:
                    b = -1
                    result = 1
                    break
                temp.append(j)
    print('#{} {}'.format(tc, result))