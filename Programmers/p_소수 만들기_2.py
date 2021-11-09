from itertools import combinations as combi

def solution(nums):
    answer = 0
    for triple in combi(nums, 3):
        n = sum(triple)
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            answer += 1
    return answer