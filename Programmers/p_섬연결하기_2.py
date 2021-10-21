def solution(n, costs):

    def find_parent(parent, n):
        if parent[n] != n:
            parent[n] = find_parent(parent, parent[n])
        return n
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    answer = 0 
    costs.sort(key=lambda x:x[2])  # 비용 기준으로 오름차순 정렬
    parent = [i for i in range(n)]

    for node_a, node_b, cost in costs:
        if find_parent(parent, node_a) != find_parent(parent, node_b):
            union_parent(parent, node_a, node_b)
            answer += cost

    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))