def dfs(x, y, arr, n):
    stack = [(x, y, 1)]
    while stack:
        a, b, dis = stack.pop()
        arr[a][b] = dis
        arr[b][a] = dis
        
        for i in range(n):
            if arr[a][i] != INF and arr[b][i] > arr[a][i] + dis:
                stack.append((b, i, dis + arr[a][i]))
            if arr[b][i] != INF and arr[a][i] > arr[b][i] + dis:
                stack.append((a, i, dis + arr[b][i]))

def solution(n, edges):
    global INF 
    INF = float('inf')
    arr = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 0

    # 각 노드의 최단거리 구하기
    for edge in edges:
        dfs(edge[0], edge[1], arr, n)
    
    answer = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or j == k: continue  # i, j, k는 서로 달라야 한다
                if arr[i][j] == arr[i][k] + arr[k][j]:
                    answer += 1
    return answer


print(solution(4, [[2,3],[0,1],[1,2]]))

# 입출력이 3 <= n <= 300000 까지라 시간초과 날 거 같다.