def factorial(k):
    result = 1
    for i in range(1, k+1):
        result *= i
    return result

n, m = map(int, input().split())
answer = factorial(n) // (factorial(n-m) * factorial(m))
print(answer)
