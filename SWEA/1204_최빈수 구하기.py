t = int(input())

for tc in range(1,t+1):
    tc = int(input())
    num_lst = list(map(int,input().split()))
    max_V = 0
    for i in num_lst:
        i_cnt = num_lst.count(i)
        if i_cnt > max_V:
            max_V = i_cnt
            res = i
    print(f'#{tc} {res}')