
# arr[x][y][0]은 기둥, arr[x][y][1]은 보 
def isValidDam(n, x, y, arr):  # x, y는 교차점
    if arr[x][y][0] == 1 or arr[x][y+1][0] == 1:  # 한쪽 끝 부분이 기둥인 경우
        return True
    elif arr[x][y][1] == 1 and arr[x][y+1][1] == 1:  # 양쪽 끝 부분 모두가 다른 보와 연결돼 있는 경우 
        return True
    return False

def isValidPillar(n, x, y, arr):
    if x == n or arr[x][y][1] == 1 or arr[x][y][0] == 1:
        return True
    return False

def removeDam(n, x, y, arr):
    # 기둥은 상관 없고 다른 보랑 연결돼 있는지 확인
    # 보 없앴다고 가정
    arr[x][y][1] = 0
    arr[x][y+1][1] = 0
    # 양 옆이 보인지 확인하기
    if 0 <= y - 1 <= n:
        if arr[x][y - 1][1] == 1:
            if not isValidDam(n, x, y-1, arr):
                return False
    if 0 <= y + 1 <= n:
        if not isValidDam(n, x, y+1, arr):
            return False
    # 제거할 수 없는 경우이므로 보 다시 원상복구
    return True

def removePillar(n, x, y, arr):
    # 기둥 없앴다고 가정
    arr[x][y][0] = 0
    arr[x-1][y][0] = 0
    if 0 <= x - 2 <= n:  # 그 위에 기둥이 또 있는지
        if arr[x-2][y][0] == 1:
            if not isValidPillar(n, x-2, y, arr):
                return False
    if arr[x-1][y][1] == 1:
        if arr[x-1][y+1][1] == 1:
            if not isValidDam(n, x-1, y, arr):
                return False
        elif arr[x-1][y-1][1] == 1:
            if not isValidDam(n, x-1, y-1, arr):
                return False
    return True

def solution(n, build_frame):
    # 우선 크기 n인 2차원 배열 만들기
    arr = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]

    for x, y, a, b in build_frame:
        # x는 열, y는 행
        x, y = n - y, x 
        # 구조물을 설치하는 경우
        if b == 1:  
            if a == 0:  # 설치할 구조물이 기둥일 때
                if isValidPillar(n, x, y, arr):
                    # 기둥은 교차점 기준 위쪽으로 설치(y -> y+1)
                    arr[x][y][0] = 1
                    arr[x-1][y][0] = 1
                
            elif a == 1:  # 설치할 구조물이 보일 때
                if isValidDam(n, x, y, arr):  # 설치 가능한 경우
                    # 보는 교차점 기준 오른쪽으로 설치(x -> x+1)
                    arr[x][y][1] = 1
                    arr[x][y+1][1] = 1
        # 구조물을 제거하는 경우
        elif b == 0:
            if a == 0:  # 제거할 구조물이 기둥일 때
                if not removePillar(n, x, y, arr):  # 제거할 수 없는 경우면 제거했던 기둥 복상복구
                    arr[x][y][0] = 1
                    arr[x-1][y][0] = 1
            elif a == 1:  # 제거할 구조물이 보일 때
                if not removeDam(n, x, y, arr):  # 제거할 수 없는 경우면 제거했던 보 복상복구
                    arr[x][y][1] = 1
                    arr[x][y+1][1] = 1

    answer = []
    for j in range(n+1):
        for i in range(n, -1, -1):
            # 기둥이 있을 때
            if arr[i][j][0] == 1:
                if 0 <= i-1 <= n and arr[i-1][j][0] == 1:
                    # 그 위에도 기둥이면
                    answer.append([j, n-i, 0])
                    arr[i][j][0] = 0
                    # arr[i-1][j][0] = 0
    for i in range(n+1):
        for j in range(n+1):
            # 보 일때
            if arr[i][j][1] == 1:
                if 0 <= j+1 <= n and arr[i][j+1][1] == 1:
                    # 그 오른쪽도 보이면
                    answer.append([j, n-i, 1])
                    arr[i][j][1] = 0
                    # arr[i][j+1][1] = 0
    answer.sort()
    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))