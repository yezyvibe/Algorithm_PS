def solution(n):
    col = [0] * (n+1)
    diagonal_up = [0] * (2 * n - 1)   # 상향 
    diagonal_down = [0] * (2 * n - 1)   # 하향
    cnt = 0
    def check(r):
        nonlocal cnt, n
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
    check(0)
    return cnt