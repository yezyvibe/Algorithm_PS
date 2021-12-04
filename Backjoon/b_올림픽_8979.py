import sys
from collections import deque


input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
country = []
for i in range(n):
    c, g, s, b = map(int, input().rstrip().split())
    country.append((g,s,b,c))
country.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

res = {}
rank = 1
tmp = 0
country = deque(country)
while country:
    cur = country.popleft()
    res[cur[3]] = rank
    if country and country[0][:3] != cur[:3]:
        rank += (tmp+1)
        tmp = 0
    else:
        tmp += 1
print(res[k])