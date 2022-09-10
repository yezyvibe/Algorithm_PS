def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    target_sum = (sum1 + sum2) // 2

    new_queue = queue1 + queue2
    new_queue_len = len(new_queue)
    start, end = 0, len(queue1) - 1
    cnt = 0
    while sum1 != target_sum:
        if sum1 > target_sum:
            sum1 -= new_queue[start]
            start += 1

        elif sum1 < target_sum:
            end += 1
            if end >= new_queue_len:
                return - 1
            sum1 += new_queue[end]
        cnt += 1
    return cnt 

queue1, queue2 = [1, 1], [1, 5]
print(solution(queue1, queue2))