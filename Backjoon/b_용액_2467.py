import sys


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
start, end = 0, n - 1
result = 2000000000
answer = []

while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < result:
        result = abs(tmp)
        answer = [arr[start], arr[end]]
    if tmp > 0:
        end -= 1
    else:
        start += 1
print(*answer)