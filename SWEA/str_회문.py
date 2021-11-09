t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = [list(input()) for l in range(n)]
    result = ''
# 가로
    for a in arr:
        for i in range(n-m+1):
            b = a[i:i+m]
            if b[:len(b)//2] == b[-1:-(len(b)//2)-1:-1]:
                result = b
                break
# 세로
    for j in range(n):
        for k in range(j,n):
            arr[k][j],arr[j][k] = arr[j][k],arr[k][j]

    for a in arr:
        for i in range(n-m+1):
            b = a[i:i+m]
            if b[:len(b)//2] == b[-1:-(len(b)//2)-1:-1]:
                result = b
                break

    print('#{} {}'.format(tc, ''.join(result)))