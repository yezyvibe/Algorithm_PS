import sys

input = sys.stdin.readline
n, m = map(int, input().split(' '))
n_l = set()
n_s = set()
for _ in range(n):
    name = input().rstrip()
    n_l.add(name)
for _ in range(m):
    name = input().rstrip()
    n_s.add(name)

res = sorted(list(n_l & n_s))
print(len(res))
for i in res:
    print(i)