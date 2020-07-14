def solution(n):
    answer = 0
    arr = [0] * (n+1)
    for i in range(2, n+1):
        if arr[i] == 1:
            continue
        for k in range(2, i+1):
            if i % k == 0:
                if i != k:
                    arr[i] = 1
                    break
        else:
            answer += 1
        for j in range(i, n+1, i):
            arr[j] = 1
    return answer
