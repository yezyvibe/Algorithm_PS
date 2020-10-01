def solution(arr):
    answer = 0
    arr.sort()
    max = arr[-1]
    answer = max
    while True:
        for i in range(len(arr)-1):
            if answer % arr[i] != 0:
                break
        else:
            return answer
        answer += max