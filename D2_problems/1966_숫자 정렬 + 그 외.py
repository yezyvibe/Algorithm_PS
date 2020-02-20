t = int(input())

for tc in range(1, t+1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum_lst = []
    res = 0
    if n <= m:
        for i in range(m-n+1):
            mul_sum = 0
            sample_b = b[i:i+n]
            for j in range(n):
                mul = a[j]*sample_b[j]
                mul_sum += mul
            sum_lst.append(mul_sum)
        res = max(sum_lst)
    else:
        for i in range(n-m+1):
            mul_sum = 0
            sample_a = a[i:i+m]
            for j in range(m):
                mul = b[j]*sample_a[j]
                mul_sum += mul
            sum_lst.append(mul_sum)
        res = max(sum_lst)

    print('#{} {}'.format(tc,res))

