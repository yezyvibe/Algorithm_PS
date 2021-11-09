import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().rstrip().split(' ')))
t_b = list(map(int, input().rstrip().split(' ')))
b = []

for idx, val in enumerate(t_b):
    b.append((val, idx))

a.sort()
b.sort(key=lambda x: -x[0])
res = 0
for i in range(n):
    tmp = a[i] * b[i][0]
    res += tmp
print(res)
