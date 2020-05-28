def dfs(start, cnt):
    global res
    if cnt == min_cnt:
        if check():
            res = cnt
        return
    for i in range(start, h):
        for j in range(n-1):
            if not ladder[i][j-1] + ladder[i][j] + ladder[i][j+1]:
                ladder[i][j] = 1
                dfs(i, cnt+1)
                ladder[i][j] = 0

def check():
    # h행 n열, 1열부터 시작
    for j in range(n):
        tmp = j
        for i in range(h):
            if ladder[i][tmp]: # 이어져 있으면 오른쪽으로 열 한칸 이동
                tmp += 1
            elif ladder[i][tmp-1]: # 왼쪽방향이 이어져 있는 지 확인
                tmp -= 1 # 왼쪽으로 열 이동

        # 모든 행을 거친 뒤 자기 원래 열 번호(j)로 돌아오지 않으면 False
        if tmp != j:
            return False
    # 모든 열이 사다리를 타고 자기 열 번호로 돌아온다면 True 반환
    return True

n, m, h = map(int, input().split())
ladder = [[0]*n for _ in range(h)]
for i in range(m):
    # a 행 b 열
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

res = 10000
for min_cnt in range(4):
    dfs(0, 0)
    if res != 10000:
        print(res)
        break
else:
    print(-1)
