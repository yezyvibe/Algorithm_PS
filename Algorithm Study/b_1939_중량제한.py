from collections import deque
import sys

input = sys.stdin.readline


def bfs(s, weight):
    q = deque()
    visit = [0 for _ in range(n)]
    q.append(s)
    visit[s] = 1
    while q:
        x = q.popleft()
        for nx, w in arr[x]:
            if visit[nx] == 0 and w >= weight:
                visit[nx] = 1
                q.append(nx)

    if visit[y - 1] == 1:
        return True


n, m = map(int, input().split())
arr = [[] for _ in range(n)]

for _ in range(m):  # 인접 리스트
    a, b, c = map(int, input().split())
    arr[a - 1].append([b - 1, c])
    arr[b - 1].append([a - 1, c])

# print(arr)
x, y = map(int, input().split())

start, end = 1, 0
for i in arr[y - 1]:
    end = max(end, i[1])

while start <= end:  # 이분탐색
    mid = (start + end) // 2
    if bfs(x - 1, mid):  # 가능한 경우
        answer = mid
        start = mid + 1
    else:  # 불가능
        end = mid - 1

print(answer)
