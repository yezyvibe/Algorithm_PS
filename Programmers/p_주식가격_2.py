from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    while q:
        now = q.poplet()
        time = 0
        for next in q:
            time += 1
            if now > next:
                break
        answer.append(time)
    return answer 

#https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python
# 효율성 시간 초과       
# def solution(prices):
#     answer = [0]*len(prices)
#     for i in range(len(prices)):
#         front = prices[i]
#         cnt = 0
#         for price in prices[i+1:]:
#             cnt += 1
#             if front > price:
#                 break
#         answer[i] = cnt
#     return answer