from itertools import combinations as combi
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        info = info.split()
        info_key = info[:-1]
        info_val = int(info[-1])
        for i in range(5):
            for c in combi(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)

    for key in info_dict.keys():
        info_dict[key].sort()
    
    for query in queries:
        query = query.split(' and ')
        food_score = query.pop()
        food_score = food_score.split(' ')
        food, score = food_score[0], food_score[1]
        query.append(food)
        while '-' in query:
            query.remove('-')
        query = ''.join(query)
        
        if query in info_dict:
            score_list = info_dict[query]
            if score_list:
                start, end = 0, len(score_list)
                while end > start:
                    mid = (start + end) // 2
                    if score_list[mid] >= int(score):
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score_list)-start)
        else:
            answer.append(0)
    return answer

# 정확성만 통과한 코드
# def solution(info, query):
#     answer = []
#     for q in query:
#         q = q.split(' and ')
#         food_score = q.pop()
#         food_score = food_score.split(' ')
#         q.append(food_score[0])
#         q.append(food_score[1])
#         language, job_group, career, food, score =  q[0], q[1], q[2], q[3], q[4]
#         cnt = 0
#         for i in info:
#             i = i.split(' ')
#             if language != '-':
#                 if language != i[0]:
#                     continue
#             if job_group != '-':
#                 if job_group != i[1]:
#                     continue
#             if career != '-':
#                 if career != i[2]:
#                     continue
#             if food != '-':
#                 if food != i[3]:
#                     continue
#             if score != '-':
#                 if int(score) > int(i[4]):
#                     continue
#             cnt += 1
#         answer.append(cnt)
#         print(answer)
#     return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))