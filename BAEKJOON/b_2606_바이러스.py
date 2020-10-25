import sys

input = sys.stdin.readline
n = int(input())
adj = [[] * (n + 1) for _ in range(n + 1)]

# 인접행렬
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    adj[a].append(b)
    adj[b].append(a)
# dfs
s = [1]
v = [0] * (n + 1)
v[1] = 1
while s:
    node = s.pop()
    for i in adj[node]:
        if not v[i]:
            s.append(i)
            v[i] = 1
print(sum(v) - 1)
