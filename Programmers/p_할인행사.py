def solution(want, number, discount):
    answer = 0
    want_dict = {}
    discount_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    for i in range(len(discount)):
        cur = discount[i]
        if cur in discount_dict:
            discount_dict[cur] += 1
        else:
            discount_dict[cur] = 1
        
        if i < 9:
            continue

        if i >= 10:
            deleted = discount[i-10]
            if deleted in discount_dict:
                discount_dict[deleted] -= 1
                if discount_dict[deleted] == 0:
                    discount_dict.pop(deleted)
        # 모두 할인하는지 확인
        for key, value in want_dict.items():
            if key not in discount_dict or discount_dict[key] != value:
                # 할인 불충분
                break
        else:
            # 할인 충족
            answer += 1
    return answer

# from collections import Counter

# def solution(want, number, discount):
#     answer = 0
#     dic = {}
#     for i in range(len(want)):
#         dic[want[i]] = number[i]
    
#     for i in range(len(discount)-9):
#         if dic == Counter(discount[i:i+10]):
#             answer += 1
#     return answer



print(solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))