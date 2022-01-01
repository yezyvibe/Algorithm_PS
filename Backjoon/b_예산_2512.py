import sys

def binary_search(total_budget):
    start = 0
    end = budget_request[-1]
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tmp_total = 0
        for i in range(len(budget_request)):
            if budget_request[i] <= mid:
                tmp_total += budget_request[i]
            else:
                tmp_total += mid
        if tmp_total > total_budget:
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer
    

input = sys.stdin.readline
N = int(input())
budget_request = list(map(int, input().split()))
total_budget = int(input())
budget_request.sort()
print(binary_search(total_budget))
