t = int(input())
for tc in range(1,t+1):
    lst_sum = 0
    num_lst = list(map(int,input().split()))
    max_v = max(num_lst)
    min_v = min(num_lst)
    num_lst.remove(max_v)
    num_lst.remove(min_v)

    for l in num_lst:
        lst_sum += l

    a = lst_sum / len(num_lst)
    res = round(a)
    print('#{} {}'.format(tc, res))