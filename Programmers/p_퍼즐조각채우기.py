def solution(game_board, table):
    # 도형의 칸수만큼 딕셔너리로 도형의 위치 저장하기
    # 딕셔너리 밸류값은 이차원 배열 = [[도형 한개의 4가지 방향], [...]]
    L = len(game_board)
    visit = [[0]*L for _ in range(L)]
    visited = [[0]*L for _ in range(L)]

    def search_shape(a, b, n, chk):
        visit[a][b] = 1
        stack = [(a, b)]
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        result = [(0, 0) if not chk else (a, b)]

        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if  0 <= nx < n and 0 <= ny < n:
                    if not visit[nx][ny] and table[nx][ny] == 1 and not chk:
                        stack.append((nx, ny))
                        result.append((nx-a, ny-b))
                        visit[nx][ny] = 1
                    if not visited[nx][ny] and game_board[nx][ny] == 0 and chk:
                        stack.append((nx, ny))
                        result.append((nx, ny))
                        visited[nx][ny] = 1        
        return result

    shape_dict = {}
    for i in range(L):
        for j in range(L):
            if table[i][j] == 1 and not visit[i][j]:
                # 도형 탐색 시작    
                res = search_shape(i, j, L, False)
                cnt = len(res)
                if cnt not in shape_dict:
                    shape_dict[cnt] = [res]
                else:
                    shape_dict[cnt].append(res)

    def rotate(arr):
        n = len(arr)
        rotate_arr = [[0]*n for _ in range(n)]
        # for a in arr:
        #     print(a)
        # print("변경전1")
        for i in range(n):
            for j in range(n):
                rotate_arr[j][n - 1 - i] = arr[i][j]
        # for a in rotate_arr:
        #     print(a)
        # print("변경후1")
        return rotate_arr

    def search(a, b, res ,candidates):
        res.sort(key=lambda x:(x[0], x[1]))
        # candidates.sort(key=lambda x:(x[0], x[1]))
        gap_a = -a
        gap_b = -b
        for i in range(len(candidates)):
            candidates[i].sort(key=lambda x:(x[0], x[1]))
            for j in range(len(candidates[i])):
                origin = res[j][0]+gap_a, res[j][1]+gap_b
                compare = candidates[i][j]
                if origin != compare:
                    break
            else:
                # 동일함
                del shape_dict[len(res)][i]
                return True
        return False
    
    def restore_visit(ls):
        for a, b in ls:
            visited[a][b] = 0

    def change(a, b, n):
        stack = [(a, b)]
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        while stack:
            x, y = stack.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if  0 <= nx < n and 0 <= ny < n:
                    if game_board[nx][ny] == 0: 
                        game_board[nx][ny] = 2
                        stack.append((nx, ny))

    answer = 0
    for i in range(4):
        if i != 0:
            game_board = rotate(game_board)
            visited = rotate(visited)
        for i in range(L):
            for j in range(L):
                if game_board[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = 1
                    res = search_shape(i, j, L, True)
                    key = len(res)
                    if key in shape_dict:
                        if search(i, j, res, shape_dict[key]):
                            visited[i][j] = 1
                            answer += key
                            change(i, j, L)
                        else:
                            restore_visit(res)
                    else:
                        restore_visit(res)
                
    return answer

print(solution(	[[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))