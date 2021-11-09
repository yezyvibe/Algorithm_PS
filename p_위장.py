def solution(clothes):
    dict = {}
    answer = 1
    for cloth, type in clothes:
        if type not in dict:
            dict[type] = [cloth]
        else:
            dict[type].append(cloth)

    for type in dict.keys():
        answer *= len(dict[type]) + 1

    return answer - 1
            
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))