from collections import deque 


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    target_sum = (sum1 + sum2) // 2
    cnt = 0

    if max(queue1) > target_sum or max(queue2) > target_sum :
        return -1

    while sum1 != sum2:
        if sum1 > sum2:
            cur = queue1.popleft()
            sum1 -= cur
            queue2.append(cur)
            sum2 += cur
        else:
            cur = queue2.popleft()
            sum2 -= cur
            queue1.append(cur)
            sum1 += cur
        cnt += 1
        
        if cnt >= 300000 * 2:
            return -1
    return cnt 

queue1, queue2 = [3,2,7,2], [4,6,5,1]
print(solution(queue1, queue2))