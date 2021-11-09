def search(arr):
    global cnt
    for i in range(N):
        j = 0
        check = 1
        while j < N - 1:
            if arr[i][j] == arr[i][j+1]:
                j += 1
                continue

            # 높은 곳에서 낮은 곳으로 향하는 경사로
            elif arr[i][j] - arr[i][j+1] == 1:
                if arr[i][j+1:j+1+L].count(arr[i][j+1]) == L:
                    visit[i][j+1:j+1+L] = [1]*L
                    j = j+L
                    continue
                else:
                    check = 0
                    break
            # 낮은 곳에서 높은 곳으로 향하는 경사로
            elif arr[i][j] - arr[i][j+1] == -1:
                if arr[i][j+1-L:j+1].count(arr[i][j])==L and True not in visit[i][j+1-L:j+1]:
                    visit[i][j+1-L:j+1] = [1]*L
                    j += 1
                    continue
                else:
                    check = 0
                    break
            else:
                check = 0
                break

        if check == 1:
            cnt += 1

N, L = map(int, input().split())
arr_garo = [list(map(int, input().split())) for _ in range(N)]
arr_sero = list(map(list, list(zip(*arr_garo))))
cnt = 0
visit = [[0]*N for _ in range(N)]
search(arr_garo)
visit = [[0]*N for _ in range(N)]
search(arr_sero)
print(cnt)