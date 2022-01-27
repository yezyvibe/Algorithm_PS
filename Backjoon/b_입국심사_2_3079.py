import sys


input = sys.stdin.readline
n, m = map(int, input().split())
immigration = [int(input()) for _ in range(n)]
immigration.sort()
start, end = 1, immigration[-1]*m
answer = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in immigration:
        tmp += mid // i

    if tmp >= m:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)