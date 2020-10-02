from itertools import combinations as combi


def solution(nums):
    answer = 0
    c_lst = list(combi(nums, 3))

    for c in c_lst:
        s = sum(c)
        for i in range(2, s):
            if s % i == 0:
                break
        else:
            answer += 1
    return answer