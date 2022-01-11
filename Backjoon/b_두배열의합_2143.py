from collections import defaultdict
import sys

input = sys.stdin.readline
T = int(input())
n = int(input())
A_arr = list(map(int, input().split()))
m = int(input())
B_arr = list(map(int, input().split()))

A_dict = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        A_dict[sum(A_arr[i:j+1])] += 1

answer = 0
for i in range(m):
    for j in range(i, m):
        answer += A_dict[T - sum(B_arr[i:j+1])]
print(answer)