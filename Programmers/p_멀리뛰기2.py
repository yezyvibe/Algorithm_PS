def solution(n):
    step = [0] * (n+1)
    step[0], step[1] = 1, 1

    for i in range(2, n+1):
        step[i] = step[i-1] + step[i-2]
    
    return step[n] % 1234567