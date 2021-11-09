t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = [list(map(int, input().split())) for l in range(n)]
    sum_lst = []
    for i in range(0,n-m+1):
        for j in range(0,n-m+1):
            a_lst = []
            for k in range(m):
                for o in range(m):
                    a_lst.append(arr[i+k][j+o])
            sum_lst.append(sum(a_lst))
    result = max(sum_lst)

    print('#{} {}'.format(tc, result))