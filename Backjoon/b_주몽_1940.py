import sys
from itertools import combinations as combi


input = sys.stdin.readline
n = int(input())
m = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
answer = 0
left, right = 0, n-1
while left < right:
    if n_list[left] + n_list[right] == m:
        answer += 1
        left += 1
        right -= 1
    elif n_list[left] + n_list[right] < m:
        left += 1
    elif n_list[left] + n_list[right] > m:
        right -= 1
print(answer)