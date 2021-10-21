
#https://velog.io/@jujube0/Programmers-%ED%81%AC%EB%A3%A8%EC%8A%A4%EC%B9%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%84%AC-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0
# 최소 스패닝 트리(MST), 크루스칼 알고리즘

def solution(n, costs):
    answer = 0
    
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트가 아니라면 찾을 때까지 재귀 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 찾기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    # 부모 테이블
    parent = [0] * n
    # 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i
    
    # 크루스칼 알고리즘을 위해 비용순으로 정렬
    costs = sorted(costs, key=lambda x:x[2])
    
    # 크루스칼 알고리즘 수행
    # 간선을 하나씩 확인하며
    for edge in costs:
        a, b, cost = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    
    return answer


def solution(n, costs):
    answer = 0

    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    costs = sorted(costs, key=lambda x:x[2])

    for edge in costs:
        a, b, cost = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost
    
    return answer

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    costs.sort(key = lambda x : x[2])
    price = 0
    count = 0
    for s,e,c in costs:
        if find(s) != find(e):
            union(s,e)
            price += c
            count += 1
            if count == n + 1:
                return price

    return price
            
        
    
    return answer



def solution(n, costs):
    costs = sorted(costs, key=lambda x:x[2])
    node = set([costs[0][0], costs[0][1]])
    answer = costs[0][2]

    while len(node) != n:
        for i in range(1, len(costs)):
            if costs[i][0] in node and costs[i][1] in node:
                continue
            if costs[i][0] in node or costs[i][1] in node:
                node.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                break
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))