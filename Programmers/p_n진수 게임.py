def change(num, n):
    numbers = '0123456789ABCDEF'
    r = ''
    if num == 0:
        return '0'
    while num > 0:
        r = numbers[num % n] + r
        num = num // n
    return r

def solutuon(n, t, m, p):
    answer = ''
    for i in range(t*m):
        answer += change(i, n)

    return answer