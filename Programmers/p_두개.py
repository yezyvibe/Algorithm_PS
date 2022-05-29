# 실제 연산을 하나하나 다 실행하기 되면 비효율적 
def solution(queue1, queue2):
    new_queue = queue1 + queue2
    sum_1, sum_2 = sum(queue1), sum(queue2) 
    target_sum = (sum_1 + sum_2) // 2
    mid = len(new_queue) // 2
    start, end, cur_sum = 0, 0, 0
    answer = float("INF")
    while start <= end and end <= len(new_queue):
        if cur_sum == target_sum:
            # 연산 세기
            tmp = 0
            if mid < end:
                tmp += (end - mid)
                tmp += (start)
                answer = min(tmp, answer)
                
            elif end <= mid:
                tmp += (mid - start)
                tmp += (len(new_queue) - end - 1)
                answer = min(tmp, answer)
            cur_sum -= new_queue[start]
            start += 1
        elif cur_sum > target_sum:  # 크면 앞에꺼 빼주고
            cur_sum -= new_queue[start]
            start += 1
        elif cur_sum < target_sum:  # 작은면 뒤에꺼 넣어주고
            if end == len(new_queue):
                break
            cur_sum += new_queue[end]
            end += 1
    return answer


print(solution([1, 6, 5, 4, 1]	, [3, 2, 5, 2, 1]))