n = int(input())
def w(n):
    if n == 1:
        print(1)
        return
    elif n % 2 == 1:
        print(n)
        n = 3*n+1
        w(n)
    else:
        print(n)
        n = n//2
        w(n)

w(n)
