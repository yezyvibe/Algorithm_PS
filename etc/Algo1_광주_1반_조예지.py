def dfs(i, j):

    # i행 탐색
    for a in range(len(arr[i])):
        if arr[i][a] == 0:
            pass
        elif arr[i][a] in arr[i][a+1::]:
            return False

    # j열 탐색
    for a in range(len(arr[i])):
        tmp = arr[a][j]
        for b in range(a+1, len(arr[i])):
            if tmp == 0:
                pass
            elif tmp == arr[b][j]:
                return False

    # 3X3 사각형 탐색
    visit = [0]*(len(arr[i])+1) # 사각형 내 중복값이 있는 지 확인하기 위한 리스트 생성
    for a in range_check(i):
        for b in range_check(j):
            tmp = arr[a][b]
            if tmp == 0:
                pass
            elif visit[tmp]: # 이미 중복된 값이 존재하면 False 반환으로 함수 끝내기
                return False
            elif not visit[tmp]: # 중복된 값이 없다면 visit 리스트의 해당 리스트 값 1로 바꾸기
                visit[tmp] = 1
    return True

# 주어진 행열 번호를 가지고, 3X3 사각형의 범위를 찾기 위한 함수
def range_check(k):
    if i in range(0,3):
        return range(0,2)
    elif i in range(3,6):
        return range(3,6)
    elif i in range(6,9):
        return range(6,9)

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(9)]
    cnt = 0
    check = 0
    for _ in range(n):
        # i행 j열
        i, j, k = map(int, input().split())
        arr[i][j] = k
        if check: # 남은 인풋을 정상적으로 입력받기 위한 장치
            continue
        elif dfs(i, j): # dfs함수를 모두 돌아 스도쿠 값으로 인정되면 cnt 1 증가
            cnt += 1
        elif not dfs(i, j): # dfs함수를 돌다가 어느 한 곳에서 스도쿠가 못 되는 결격사유가 발생하면 check = 1로 바꿔서
            check = 1       # 나머지 인풋이 dfs 함수 돌지 못하게 해주는 장치
    print('#{} {}'.format(tc, cnt))
