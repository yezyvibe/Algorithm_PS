def solution(n):
    a, b = 0, 1
    for i in range(n-1):
        c = (a + b) % 1234567
        tmp = a
        a = b
        b = tmp + b
    return c

# def solution(n):
#     a, b = 0, 1
#     res = 0
#     def fibo(a, b, n, k):
#         nonlocal res
#         if k == n:
#             return
#         else:
#             c = a + b
#             res = c
#             fibo(b, c, n, k+1)
#     fibo(a, b, n, 1)
#     return res % 1234567

