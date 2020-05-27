import sys
input = sys.stdin.readline

def dfs(adj, start, parent):
    s = [start]
    while s:
        tmp = s.pop()
        for i in adj[tmp]:
            # 부모 리스트에 i의 부모로 tmp를 넣어주고
            parent[i].append(tmp)
            s.append(i)
            # i의 인접 리스트에는 tmp를 제거해주기(중복 없애기 위해)
            adj[i].remove(tmp)
    return parent

n = int(input())
adj = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
# 인접리스트 만들기
for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

result = dfs(adj, 1, parent)

# 2번 노드부터 결과값만 출력
for i in range(2,n+1):
    print(result[i][0])