def solution(n):
    answer = 0
    arr = [0] * (n+1)
    for i in range(2, n+1):
        if arr[i] == 1:
            continue
        answer += 1
        for k in range(i, n+1, i):
            arr[k] = 1

    return answer
