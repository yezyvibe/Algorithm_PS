import sys
from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(len(arr)):
    target = arr[i]
    tmp = arr[:i] + arr[i+1:]
    start, end = 0, n - 2
    while start < end:
        sum = tmp[start] + tmp[end]
        if sum == target:
            answer += 1
            break
        if sum < target:
            start += 1
        else:
            end -= 1
print(answer)