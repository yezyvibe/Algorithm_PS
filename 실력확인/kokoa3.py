from itertools import product

def solution(users, emoticons):
    m = len(emoticons)
    discounts = [10, 20, 30, 40] 
    cases = list(product(discounts, repeat = m))
    answer = []
    for i in range(len(cases)):
        cur_case = cases[i]
        subscriber, profit = 0, 0
        for j in range(len(users)):
            rate, money = users[j]
            # rate 이상 이모티콘 구매 한다.
            # money 이상이면 이모티콘 플러스 가입
            tmp = 0
            for k in range(len(cur_case)):
                # 해당 이모티콘 할인율
                if cur_case[k] >= rate:
                    tmp += (emoticons[k] * (100 - cur_case[k])* 0.01)
                    if money <= tmp: # 예산 초과면 이모티콘 가입, 그 동안 샀던 금액 회수
                        subscriber += 1
                        profit -= tmp
                        break
            profit += tmp
        answer.append([subscriber, int(profit)])
    answer.sort(key=lambda x:(x[0], x[1]))
    return answer[-1]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))