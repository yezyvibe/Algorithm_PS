n = int(input())
def factorial(n, fac):
    if n == 1:
        print(fac)
    else:
        fac *= n
        factorial(n-1,fac)

fac = 1
factorial(n, fac)