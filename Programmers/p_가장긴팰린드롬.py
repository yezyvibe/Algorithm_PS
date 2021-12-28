def solution(s):
    answer = 1
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            print(s[i:j], i, j)
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, len(s[i:j]))
    return answer


s = "abacde"
print(solution(s))


# 다른 풀이
# def longest_palindrom(s):
#     for i in range(len(s),0,-1):
#         for j in range(len(s)-i+1):
#             if s[j:j+i] == s[j:j+i][::-1]:
#                 return i