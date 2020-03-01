n = int(input())
res = []
def triangle(n):
    if n != 1:
        res.append('*' * n)
        n -= 1
        triangle(n)
    elif n == 1:
        res.append('*')
    a = reversed(res)
    return '\n'.join(map(str, a))
print(triangle(n))
