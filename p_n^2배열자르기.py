# 시간 초과
# def solution(n, left, right):
#     # 2차원 배열 만들기
#     arr = [[0]*n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i >= j:
#                 arr[i][j] = i + 1
#             else:
#                 arr[i][j] = j + 1

#     # 1차원 배열로 변환
#     arr_list = []
#     for a in arr:
#         arr_list.extend(a)

#     return arr_list[left:right+1]


def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        answer.append(max(divmod(i, n))+1)
    
    return answer


n = 3
left = 2
right = 5
print(solution(n, left, right))