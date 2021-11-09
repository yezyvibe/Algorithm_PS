import sys

input = sys.stdin.readline
n = int(input())

adj = [[] for _ in range(n + 1)]
for i in range(int(input())):
    a, b = map(int, input().split(' '))
    adj[a].append(b)
    adj[b].append(a)

invite = [0] * (n + 1)
for i in adj[1]:
    invite[i] = 1
    for j in adj[i]:
        if not invite[j]:
            invite[j] = 1

print(sum(invite) - 1)
