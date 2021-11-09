# from itertools import combinations as combi
# from collections import deque
# from copy import deepcopy


# def candidate_key_check(key_list, relation):
#     res = []
#     for r in relation:
#         tmp = ''
#         for i in key_list:
#             tmp += r[i]
#         res.append(tmp)
#     if len(res) == len(set(res)):
#         return True
#     return False

# def solution(relation):
#     possible_key = deque()
#     for i in range(1, len(relation[0])+1):
#         for c in combi([i for i in range(len(relation[0]))], i):
#             if candidate_key_check(list(c), relation):
#                 possible_key.append(list(c))

#     while True:
#         a = possible_key.popleft()
#         res_list = deque()

#         for i in range(len(possible_key)):
#             for k in range(len(possible_key[i])-len(a)+1):
#                 tmp = possible_key[i][k:k+len(a)]
#                 if a == tmp:
#                     break
#             else:
#                 res_list.append(possible_key[i])
#         else:
#             if len(possible_key) == len(res_list):
#                 possible_key.append(a)
#                 break
#             possible_key = deepcopy(res_list)
#             possible_key.append(a)
            
    
#     return len(possible_key)


from itertools import combinations as combi

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    candidates = []
    for i in range(1, col+1):
        candidates.extend(combi(range(col), i))

    unique = []
    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candidate)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
   
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))