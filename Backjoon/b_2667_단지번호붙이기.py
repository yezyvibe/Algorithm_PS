#dfs 로 풀기

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i,j):
    global cnt
    cnt += 1
    q = []
    q.append((i, j))
    check = 0

    while q:
        x, y = q.pop(0)
        arr[x][y] = 2
        check += 1

        for k in range(4):
            if arr[x + dx[k]][y + dy[k]] == 1:
                arr[x + dx[k]][y + dy[k]] = 2
                q.append((x+dx[k], y+dy[k]))

    num_list.append(check)

n = int(input())
arr = [[0]+list(map(int, input()))+[0] for l in range(n)]
zz = [[0]*(n+2)]
arr = zz+arr+zz
num_list = []
cnt = 0

for i in range(n+2):
    for j in range(n+2):
        if arr[i][j] == 1:
            bfs(i, j)

print(cnt)
num_list.sort()
for i in num_list:
    print(i)
