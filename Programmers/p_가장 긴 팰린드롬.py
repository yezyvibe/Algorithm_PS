# 최종 코드
def solution(s):
    origin_len = len(s)
    n = len(s)
    idx = 0

    while True:
        tmp = s[idx:idx + n]
        if tmp == tmp[::-1]:
            return n
        idx += 1
        if idx + n > origin_len:
            n -= 1
            idx = 0

# 참고 풀이
# def pal(s):
#     for i in range(len(s), -1, -1):
#         for j in range(len(s) - i + 1):
#             # print(s[j:j+i])
#             word = s[j:j + i]
#             revers_word = word[::-1]
#             if word == revers_word:
#                 # print(word)
#                 return len(word)

# 효율성 1번 시간초과 났음
# def solution(s):
#     answer = 0
#     answer = pal(s)
#
#     return answer
#
#
# import math
#
#
# def solution(s):
#     s = list(s)
#     origin_len = len(s)
#     n = len(s)
#     idx = 0
#
#     while True:
#         tmp = s[idx:idx + n]
#         if n % 2 == 0:
#             mid = n // 2
#             f, b = tmp[:mid], tmp[mid:]
#             for i in range(len(f)):
#                 if f[i] != b[len(b) - 1 - i]:
#                     idx += 1
#                     break
#             else:
#                 return n
#         else:
#             mid = math.floor(n / 2)
#             f, b = tmp[:mid], tmp[mid + 1:]
#             for i in range(len(f)):
#                 if f[i] != b[len(b) - 1 - i]:
#                     idx += 1
#                     break
#             else:
#                 return n
#
#         if idx + n > origin_len:
#             n -= 1
#             idx = 0
#
# s = "abcdcba"
# print(solution(s))

