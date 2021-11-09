a, b = map(int,input().split())

def odd(a,b):
    if a == b+1:
        return
    elif a % 2 == 1:
        print(a, end=' ')
        odd(a+1,b)
    elif a % 2 != 1:
        odd(a+1,b)
odd(a,b)