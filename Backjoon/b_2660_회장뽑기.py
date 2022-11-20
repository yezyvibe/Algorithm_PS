import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

def dfs(s):
    q = deque([s])
    visit = [0] * (n+1)
    visit[s] = 1

    while q:
        x = q.popleft()

        for next in friends[x]:
            if not visit[next]:
                visit[next] = visit[x] + 1
                q.append(next)
    
    return max(visit)


friends = [[] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())

    if a == b == -1:
        break

    friends[a].append(b)
    friends[b].append(a)



min_value = float('inf')
candidates = []
for i in range(1, n+1):
    result = dfs(i) - 1

    if min_value > result:
        min_value = result
        candidates = [i]
    
    elif min_value == result:
        candidates.append(i)

print(" ".join(map(str, [min_value, len(candidates)])))
print(" ".join(map(str, candidates)))

