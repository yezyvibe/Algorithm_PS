# def solution(topping):
#     # 동일한 가짓수의 토핑 -> 절반을 나누는 경우의 수
#     answer = 0
#     for i in range(1, len(topping)):
#         cheolsu, brother = list(set(topping[:i])), list(set(topping[i:]))
#         if len(cheolsu) == len(brother):
#             answer += 1 
#     return answer        

# from collections import Counter

# def solution(topping):
#     dict = Counter(topping)
#     set_dict = set()
#     answer = 0

#     for i in topping:
#         dict[i] -= 1
#         set_dict.add(i) # 동생 토핑 추가
#         if dict[i] == 0: # 토핑 다 주고 나면 철수는 토핑 없어짐
#             dict.pop(i)
#         if len(dict) == len(set_dict): # 토핑 가짓수 같을 때마다 answer +=1
#             answer += 1
#     return answer


def solution(topping):
    cheolsu = {}
    brother = set()
    answer = 0

    for t in topping:
        if t in cheolsu:
            cheolsu[t] += 1
        else:
            cheolsu[t] = 1
    
    for t in topping:
        if cheolsu[t]:
            cheolsu[t] -= 1
            brother.add(t)
            if cheolsu[t] == 0:
                cheolsu.pop(t)
        if len(cheolsu) == len(brother):
            answer += 1
    return answer 
    
print(solution([1, 2, 1, 3, 1, 4, 1, 2]))



