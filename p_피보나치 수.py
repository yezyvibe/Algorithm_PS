def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)

def solution(n):
    return fibo(n) % 1234567


# def solution(num):
#     a,b = 0,1
#     for i in range(num):
#         a,b = b,a+b
#     return a % 1234567
    