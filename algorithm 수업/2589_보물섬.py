import collections
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    q = collections.deque()
    q.append([x,y])
    bg = [[0] * (s + 2) for o in range(g + 2)]
    bg[x][y] = 1
    max_v = 0

    while q:
        ax, ay = q.popleft()
        for k in range(4):
            if arr[ax+dx[k]][ay+dy[k]] == 'L' and bg[ax+dx[k]][ay+dy[k]] == 0:
                q.append([ax+dx[k], ay+dy[k]])
                bg[ax+dx[k]][ay+dy[k]] = bg[ax][ay] + 1
                if bg[ax+dx[k]][ay+dy[k]] > max_v:
                    max_v = bg[ax+dx[k]][ay+dy[k]]
    return max_v

g, s = map(int,input().split())
arr2 = [[0]+list(map(str,input()))+[0] for l in range(g)]
zz = [[0]*(s+2)]
arr = zz+arr2+zz

result =0
for i in range(1,g+1):
    for j in range(1,s+1):
        if arr[i][j] == 'L':
            b = bfs(i,j)
            if b > result:
                result = b
print(result-1)