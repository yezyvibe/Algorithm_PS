import sys 
from collections import deque
# 물을 부을 때 -> 한통이 비거나, 다른 물통이 가득 차기 
input = sys.stdin.readline


def pour(x, y):
    if not visit[x][y]:
        visit[x][y] = 1
        q.append((x, y))

def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y
        
        if x == 0: # x가 비어있을 때
            answer.append(z)
        
        # x -> y
        water = min(x, b-y)
        pour(x-water, y+water)

        # x -> z
        water = min(x, c-z)
        pour(x-water, y)

        # y -> x
        water = min(a-x, y)
        pour(x+water, y-water)

        # y -> z
        water = min(y, c-z)
        pour(x, y-water)

        # z-> x
        water = min(a-x, z)
        pour(x+water, y)

        # z -> y
        water = min(b-y, z)
        pour(x, y+water)

a, b, c = map(int, input().split())
visit = [[0]*(b+1) for _ in range(a+1)]
visit[0][0] = 1
q = deque([(0, 0)])
answer = []
bfs()
answer.sort()
print(' '.join(map(str, answer)))