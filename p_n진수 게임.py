def convert(k, n):
    base = ''
    remain = '0123456789ABCDEF'
    while k > 0:
        k, mod = divmod(k, n)
        base += remain[mod]
    base = base[::-1]
    return base

def solution(n, t, m, p):
    res = '0'
    for i in range(t*m):
        res += convert(i, n)
    cnt = 0
    answer = ''
    for i in range(p-1, len(res),m):
        cnt += 1
        answer += res[i]
        if cnt == t:
            break
    return answer    