# dp문제, 다시 풀이함
def solution(n):
    step = [0] * (n + 1)
    step[0], step[1] = 1, 1

    for i in range(2, n + 1):
        step[i] = step[i - 1] + step[i - 2]

    return step[n] % 1234567



# 시간 초과
# import math
# from itertools import permutations as p
# def solution(n):
#     cnt_1 = n
#     cnt_2 = math.ceil(n / 2)
#     num = [1 for i in range(cnt_1)] + [2 for j in range(cnt_2)]
#
#     res = set()
#     for i in range(cnt_1 + 1):
#         for k in p(num, i):
#             if sum(k) == n:
#                 res.add(k)
#     return len(res)
