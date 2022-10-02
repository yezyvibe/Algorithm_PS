import sys
sys.setrecursionlimit(10**6)

def dfs(start, group):
    visit[start] = group
    for i in arr[start]:
        if not visit[i]:
            if not dfs(i, -group):
                return False
        elif visit[i] == visit[start]:
            # 인접한 노드 두개의 집합 색이 같으면 이분 그래프 실패
            return False
    return True


input = sys.stdin.readline
K = int(input())
for i in range(K):
    V, E = map(int, input().split(" "))
    arr = [[] for _ in range(V+1)]
    for j in range(E):
        u, v = map(int, input().split(" "))
        arr[u].append(v)
        arr[v].append(u)
    
    visit= [0]*(V+1)
    # 정점 돌아가면서 탐색
    for i in range(1, V+1):
        if not visit[i] and not dfs(i, 1):
            print("NO")
            break
    else:
        print("YES")