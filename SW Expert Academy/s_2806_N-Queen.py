def backtrack(r):
    global n, cnt
    # r = 행
    if r == n:
        # 모든 행을 다 거치면 해를 찾은 것
        cnt += 1
        return

    # 열, 대각선 파악
    for c in range(n):
        # 조건에 부합하는 지 확인
        if not col[c] and not dia_1[r+c] and not dia_2[n-r+c-1]:
            col[c]=1
            dia_1[r+c]=1
            dia_2[n-r+c-1]=1
            backtrack(r+1)
            col[c]=0
            dia_1[r+c]=0
            dia_2[n-r+c-1]=0

for tc in range(1, int(input())+1):
    n = int(input())
    # 열, 대각선(상향, 하향) 확인하기 위한 리스트
    col = [0]*n
    dia_1 = [0]*(2*n-1)
    dia_2 = [0]*(2*n-1)
    cnt = 0
    backtrack(0)
    print('#{} {}'.format(tc, cnt))
