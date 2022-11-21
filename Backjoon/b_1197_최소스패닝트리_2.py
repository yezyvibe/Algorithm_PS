import sys

def union_parent(x, y):
    if x > y:
        parents[x] = y 
    else:
        parents[y] = x

def find_parents(x):
    if parents[x] != x:
        return find_parents(parents[x])
    return x

input = sys.stdin.readline
v, e = map(int, input().split())
adj = []
parents = [i for i in range(v+1)]
answer = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    adj.append((a, b, c))

adj.sort(key=lambda x:x[2])

for node_a, node_b, cost in adj:
    parent_a, parent_b = find_parents(node_a), find_parents(node_b)

    if parent_a != parent_b:
        union_parent(parent_a, parent_b)
        answer += cost

print(answer)
