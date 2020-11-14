import sys
from itertools import permutations as permu


def check(team):
    res = 0
    for i in team:
        for j in team:
            if i != j:
                res += arr[i][j]
    return res


input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
n_lst = [i for i in range(n)]
half = n // 2
min_v = 100000
for p in permu(n_lst, n):
    start = check(p[:half])
    link = check(p[half:])
    result = abs(start - link)
    min_v = min(min_v, result)
print(min_v)
