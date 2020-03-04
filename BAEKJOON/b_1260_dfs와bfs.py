def dfs(v):
    stack = []
    stack.append(v)

    while stack:
        #dfs는 pop으로 뒤에서 부터 가져옴
        current = stack.pop()
        new_adj = adj[current]
        new_adj.sort()
        new_adj.reverse()
        for neighbor in new_adj:
            if neighbor not in visited:
                stack.append(neighbor)
        if current not in visited:
            visited.append(current)

def bfs(v):
    queue = []
    queue.append(v)

    while queue:
        current = queue.pop()
        new_adj = adj[current]
        new_adj.sort()
        for neighbor in new_adj:
            if neighbor not in visited:
                queue.insert(0, neighbor)
        if current not in visited:
            visited.append(current)

# 인풋
n, m, v = map(int,input().split())
adj = [[] for _ in range(n+1)]
visited = []
result = []

# 인접리스트
for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

dfs(v)
print(*visited)
visited = []
bfs(v)
print(*visited)