import sys
from itertools import permutations as permu


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().rstrip().split(' ')))
max_v = 0
for p in permu(arr, n):
    sum = 0
    n_list = list(p)
    for i in range(1, len(n_list)):
        tmp = abs(n_list[i - 1] - n_list[i])
        sum += tmp
    max_v = max(max_v, sum)

print(max_v)
