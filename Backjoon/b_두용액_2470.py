import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, n-1
answer = 2000000000
result = []
while start < end:
    total = arr[start] + arr[end]
    if abs(total) < answer:
        answer = abs(total)
        result = [arr[start], arr[end]]
    if 0 < total:
        end -= 1
    else:
        start += 1
print(*result)

