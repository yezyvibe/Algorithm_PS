# def solution(n,a,b):
#     answer = 0

#     def next_round(num):
#         if num % 2 == 0:
#             return num // 2
#         else:
#             return num // 2 + 1

#     while True:
#         answer += 1
#         a = next_round(a)
#         b = next_round(b)
#         if a < b:
#             if b - a == 1 and b % 2 == 0:
#                 return answer
#         else:
#             if a - b == 1 and a % 2 == 0:
#                 return answer

def solution(n,a,b):
    answer = 0 
    while a != b:
        answer += 1
        a, b = (a+1) // 2, (b+1) // 2
    return answer
print(solution(8, 4, 7))