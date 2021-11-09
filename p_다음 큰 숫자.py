def solution(n):
    n_bin = bin(n)[2:].count('1')
    res = n
    while True:
        res += 1
        res_bin = bin(res)[2:].count('1')
        if n_bin == res_bin:
            return res   

print(solution(78))