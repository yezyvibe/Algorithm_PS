def convert(n):
    q = n // 3
    r = n % 3
    if q == 0:
        return str(r)
    else:
        return convert(q) + str(r)

def solution(n):
    con_n = convert(n)
    con_n = con_n[::-1]
    con_n = int(con_n, 3)
    return con_n