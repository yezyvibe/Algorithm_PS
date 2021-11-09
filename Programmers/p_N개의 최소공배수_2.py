from math import gcd

def solution(arr):
    answer = arr[0]
    arr = arr[1:]
    for num in arr:
        answer = (answer * num) / gcd(answer, num)
        print(answer)
    return answer