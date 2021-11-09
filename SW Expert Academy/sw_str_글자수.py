t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    max_v = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if j == i:
                res = cnt
                cnt += 1
            if cnt > max_v:
                max_v = cnt
    print('#{} {}'.format(tc, max_v))