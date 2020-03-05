def dfs(idx,r,c,res):
    res += str(arr[r][c])
    if idx == 6:
        n_lst.append(res)
        return
    for i in range(4):
        if 0 <= r+dx[i] < 4 and 0 <= c+dy[i] < 4:
            dfs(idx+1, r+dx[i], c+dy[i], res)

for t in range(1,int(input())+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n_lst = []
    for i in range(4):
        for j in range(4):
            s_x = i
            s_y = j
            dfs(0,s_x,s_y,'')
    result = set(n_lst)
    print(f'#{t} {len(result)}')