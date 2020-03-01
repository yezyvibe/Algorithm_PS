# def fibo(n):
#     if n < 3:
#         return 1
#     else:
#         return fibo(n-2) + fibo(n-1)
# n = int(input())
# print(fibo(n))

#
# def fibo(n):
#     if n < 3:
#         fibo_list[n] = 1
#         return 1
#     else:
#         if fibo_list[n] == 0:
#             fibo_list[n] = fibo(n-1) + fibo(n-2)
#         return fibo_list[n]
#
# n = int(input())
# fibo_list = [0]*(n+1)
# print(fibo(n) % 10009)
#
# memo = {0:1, 1:1}
#
# def fib(n):
#     if n in memo:
#         return memo[n]
#     else:
#         result = fib(n-1) + fib(n-2)
#         memo[n] = result
#         return result
# n = int(input())
# print(fib(n-1))

n = int(input())
memo = {1:1, 2:1}
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
        return memo[n]
    else:
        return memo[n]

print(fibo(n)%10009)
