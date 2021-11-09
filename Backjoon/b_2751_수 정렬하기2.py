import sys

input = sys.stdin.readline
n = int(input())
n_lst = [int(input()) for _ in range(n)]
n_lst.sort()
print('\n'.join(map(str, n_lst)))
