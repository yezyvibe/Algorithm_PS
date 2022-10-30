from typing import List

def check(target):
    cnt = 0
    while 2 ** cnt < target:
        cnt += 1
    return 2 ** cnt

def solution(queries: List[List[int]]) -> int:
    arr_dict = {}
    copy = 0
    for i in range(len(queries)):
        num, cnt = queries[i]
        if num not in arr_dict:
            arr_dict[num] = [check(cnt), cnt]
        else:
            arr_len, cur_cnt = arr_dict[num]
            next_cnt = cur_cnt + cnt
            if arr_len < next_cnt:
                copy += cur_cnt
                arr_dict[num] = [check(next_cnt), next_cnt]
            else:
                arr_dict[num][1] += cnt
    return copy


queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]
print(solution(queries))