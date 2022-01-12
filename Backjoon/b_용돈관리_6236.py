import sys

input = sys.stdin.readline
n, m = map(int, input().split())
money_list = [int(input()) for _ in range(n)]

start, end = min(money_list), sum(money_list)
max_money = max(money_list)
answer = 0
while start <= end:
    mid = (start + end) // 2  # mid는 인출한 금액 k
    current = 0
    cnt = 0
    for money in money_list:
        if money > current:
            current = mid
            cnt += 1
        current -= money
        
    if cnt > m or mid < max_money:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid
print(answer)