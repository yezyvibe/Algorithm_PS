def solution(n, m):
    answer = []
    # n이 작은 수 m이 큰 수
    if n > m:
        n, m = m, n

    for i in range(n, 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            answer.append(gcd)
            break

    lcm = m
    while True:
        if lcm % n == 0 and lcm % m == 0:
            break
        lcm += m
    answer.append(lcm)

    return answer