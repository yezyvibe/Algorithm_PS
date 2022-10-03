import sys
from itertools import combinations as combi


def dfs(group, n):
    visit = [0] * (n+1)
    stack = [group[0]]
    visit[group[0]] = 1
    while stack:
        cur = stack.pop()
        for i in adj[cur]:
            if not visit[i] and i in group:
                visit[i] = 1
                stack.append(i)
    res = 0
    for i in group:
        if not visit[i]:
            return 0
        res += people[i]
    # 해당 그룹의 인구수
    return res


input = sys.stdin.readline
n = int(input())
people = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n+1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in (tmp[1:]):
        adj[i+1].append(j)

sections = [i for i in range(1, n+1)]
INF = float('inf')
answer = INF
for i in range(1, n//2+1):
    # 두 그룹으로 나누고, 각 그룹이 연결돼 있는지 확인하기
    for c in combi(sections, i):
        a_group = list(c)
        b_group = [i for i in range(1, n+1) if i not in a_group]
        a_res = dfs(a_group, n)
        b_res = dfs(b_group, n)
        if a_res and b_res:
            # 둘 다 값이 있는 경우만 확인
            answer = min(answer, abs(a_res - b_res))
print(answer if answer != INF else -1)