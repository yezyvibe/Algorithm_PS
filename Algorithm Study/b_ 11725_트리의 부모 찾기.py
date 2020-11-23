import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split(' '))
    tree[a].append(b)
    tree[b].append(a)
# print(tree)

head = [0]*(n+1)
q = deque([1])
while q:
    parent = q.popleft()
    # print('parent:', parent)
    for child in tree[parent]:
        # print('child:', child)
        if not head[child]:
            head[child] = parent
            q.append(child)
for i in head[2:]:
    print(i)