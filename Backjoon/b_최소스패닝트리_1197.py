import sys 
input = sys.stdin.readline

def find_parent(x1):
    if parent[x1] != x1:
        return find_parent(parent[x1])
    return parent[x1]

def union_parent(x1, x2):
    if x1 < x2:
        parent[x2] = x1
    else:
        parent[x1] = x2   

v, e = map(int, input().split())
adj = []
for _ in range(e):
    a, b, c = map(int, input().split())
    adj.append([a, b, c])

adj.sort(key=lambda x:x[2])  # 비용 기준으로 오름차순 정렬
parent = [i for i in range(v+1)]
answer = 0

for node_a, node_b, cost in adj:
    parent_a, parent_b = find_parent(node_a), find_parent(node_b)
    if parent_a != parent_b:
        union_parent(parent_a, parent_b)
        answer += cost
print(answer)