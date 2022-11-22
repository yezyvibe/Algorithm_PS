import sys

def union_parent(x1, x2):
    if x1 < x2:
        parents[x2] = x1
    else:
        parents[x1] = x2

def find_parent(x):
    if x != parents[x]:
        return find_parent(parents[x])
    return parents[x]

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
parents = [i for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

arr.sort(key=lambda x:x[2])
answer = 0
edge_cnt = 0
for node_a, node_b, cost in arr:
    parent_a, parent_b = find_parent(node_a), find_parent(node_b)

    if parent_a != parent_b:
        union_parent(parent_a, parent_b)
        answer += cost
        edge_cnt += 1
        
        if edge_cnt == n-2:
            break
        
print(answer)


