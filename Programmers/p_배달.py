def solution(N, road, K):
    adj = [[] for _ in range(N)]
    for r in road:
        adj[r[0]-1].append((r[1], r[2]))
        adj[r[1]-1].append((r[0], r[2]))
    stack = [(1, 0)]
    INF = float('inf')
    check = [INF]*N
    check[0] = 0
    while stack:
        a, b = stack.pop()
        for node, time in adj[a-1]:
            if time + b <= K and check[node-1] > time + b: 
                check[node-1] = time + b
                stack.append((node, time+b))
            
    answer= 0
    for i in check:
        if i != INF:
            answer += 1
    return answer

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N,road,K))