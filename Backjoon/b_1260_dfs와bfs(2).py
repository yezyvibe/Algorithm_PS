import sys
N, M, V = map(int, sys.stdin.readline().strip().split())
edge = [[] for _ in range(N+1)]

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    edge[n1].append(n2)
    edge[n2].append(n1)

# 인접리스트 정렬 후 역순
for e in edge:
    e.sort(reverse=True)

def dfs():
    d_visit = []
    stack = [V]
    d_check = [0 for _ in range(N+1)]
    while stack:
        v1 = stack.pop()
        if not d_check[v1]:
            d_check[v1] = 1
            d_visit.append(v1)
            stack += edge[v1]
            # edge[v1]은 리스트 형태
    return d_visit

def bfs():
    b_visit= []
    queue = [V]
    b_check = [0 for _ in range(N+1)]
    # 시작점 다시 오지 않게 1 처리
    b_check[V] = 1
    while queue:
        v2 = queue.pop()
        b_visit.append(v2)
        for i in reversed(edge[v2]):
            # 작은 숫자부터 뽑아야 하니 다시 역순
            if not b_check[i]:
                b_check[i] = 1
                queue = [i] + queue
                # 리스트 안에 추가
    return b_visit

print(' '.join(map(str, dfs())))
print(' '.join(map(str, bfs())))