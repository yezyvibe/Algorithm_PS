import sys

input = sys.stdin.readline
n = int(input())
n_list = []
n_sum = 0
for i in range(n):
    weight = int(input())
    n_list.append(weight)
n_list.sort(reverse=True)

answer = 0
for i in range(len(n_list)):
    answer = max(answer, n_list[i] * (i+1))
print(answer) 