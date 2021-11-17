import sys

def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]


def union_parent(parent_a, parent_b):
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
arr.sort(key=lambda x:x[2])

edge_cnt = 0
answer = 0
parent = [i for i in range(n+1)]
for node_a, node_b, cost in arr:
    parent_a, parent_b = find_parent(node_a), find_parent(node_b)
    if parent_a != parent_b:
        union_parent(parent_a, parent_b)
        answer += cost
        edge_cnt += 1
        if edge_cnt == n-2:
            break
print(answer)