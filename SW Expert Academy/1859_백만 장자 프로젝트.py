t = int(input())

for tc in range(1,t+1):
    n = int(input())
    n_lst = list(map(int,input().split()))
    res = 0
    max_v = n_lst[-1]

    for i in range(len(n_lst)-1,-1,-1):
        if max_v > n_lst[i]:
            res += max_v - n_lst[i]
        else:
            max_v = n_lst[i]
    print(f'#{tc} {res}')

