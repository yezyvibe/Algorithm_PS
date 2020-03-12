for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    ans = -1
    for i in range(n-1):
        for j in range(i+1,n):
            num = arr[i] * arr[j]
            if ans >= num:
                break
            t = num
            b = t % 10 #일의자리
            t //= 10
            while t:
                a = t % 10 #일의자리
                if a > b:
                    break
                t //= 10
                b = a
            else:
                ans = max(ans, num)
    print('#{} {}'.format(tc, ans))

