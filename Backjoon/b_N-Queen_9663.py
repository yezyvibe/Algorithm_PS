def check(r):
    global cnt, n
    if r == n:
        cnt += 1
        return
    for c in range(n):
        if not col[c] and not diagonal_up[r+c] and not diagonal_down[n - r + c - 1]:
            col[c] = 1
            diagonal_up[r+c] = 1
            diagonal_down[n - r + c - 1] = 1
            check(r+1)
            # 배열 복구
            col[c] = 0
            diagonal_up[r+c] = 0
            diagonal_down[n - r + c - 1] = 0


n = int(input())
col = [0] * (n+1)
diagonal_up = [0] * (2*n - 1)   # 상향 
diagonal_down = [0] * (2*n - 1)   # 하향
cnt = 0
check(0)
print(cnt)



def check(x):
    # 0번 인덱스부터 차례대로니까 주어진 x까지만 검사하여 다음 퀸을 놓을 수 있는 위치를 찾는다.
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def queen(x):
    global result
    if x == n:
        result += 1
        return
    for i in range(n):
        row[x] = i
        if check(x):
            queen(x+1)  # 퀸을 놓을 수 있는 위치를 찾으면 dfs 탐색 더 진행, 못 찾는 경우면 탐색 중단


n = int(input())
result = 0
row = [0] * 15
queen(0)
print(result)



def solution(n):
    answer = 0
    chess = [[0] * n for _ in range(n)]  # 체스판
    visited = [0] * (n + 1)  # 세로칸 방문 체크

    # 조건에 일치 하는 지 체크 | 왼쪽 대각선, 오른쪽 대각선
    def check(x, y):
        ly, ry = y, y
        while x >= 0:
            x -= 1
            ly -= 1
            ry += 1
            if 0 <= ly:  # 왼쪽 대각선
                if chess[x][ly]:
                    return False

            if ry < n:  # 오른쪽 대각선
                if chess[x][ry]:
                    return False

        return True

    def bt(idx=0):
        nonlocal answer
        if idx == n:  # 체스를 마지막칸까지 두는데 성공한 경우
            answer += 1
            return

        for i in range(n):
            if visited[i] == 0:  # 세로 칸에 둔 말이 없는 경우
                if check(idx, i):  # 대각선방향 체크
                    chess[idx][i] = 1  # 체스판에 말을 두고
                    visited[i] = 1  # 이제 i 칸(세로 전체)는 말을 못둔다.
                    bt(idx + 1)
                    chess[idx][i] = 0
                    visited[i] = 0

    bt()

    return answer