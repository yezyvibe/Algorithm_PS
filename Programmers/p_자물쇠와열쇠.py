# 열쇠 차례대로, 그리고 4방향 모두 탐색
# 열쇠랑 자물쇠가 맞물리는지는 자물쇠 기준으로 확인하기

def printArr(arr):
    for a in arr:
        print(a)
    print()

def isOpen(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[N+i][N+j] != 1:
                return False
    return True

def rotateKey(keyArr, dir):
    M = len(keyArr)
    newArr = [[0] * M for _ in range(M)]

    # 원래 배열
    if dir == 0:
        return keyArr

    # 시계방향 90도 1회전
    if dir == 1:
        for i in range(M):
            for j in range(M):
                newArr[i][j] = keyArr[M -j -1][i]
        #         print(i, j, "->", M -j -1, i)
        return newArr              
    # 시계방향 180도 2회전
    if dir == 2:
        for i in range(M):
            for j in range(M):
                newArr[i][j] = keyArr[M -i -1][M-j-1]
                # print(i, j, "->", M -i -1, M-j-1)
        return newArr
    # 시계방향 270도 3회전
    if dir == 3:
        for i in range(M):
            for j in range(M):
                newArr[i][j] = keyArr[j][M-i-1]
                # print(i, j, "->",j, M-i-1)
        return newArr

def solution(key, lock):
    N = len(lock)
    M = len(key)
    arr = [[0] * (N * 3) for _ in range(N * 3)]
    
    for i in range(N):
        for j in range(N):
            arr[N+i][N+j] = lock[i][j]

    for i in range(1, N*2):
        for j in range(1, N*2):
            for d in range(4):
                key = rotateKey(key, d)
                for k in range(M):
                    for l in range(M):
                        arr[i+k][j+l] += key[k][l]
                # 자물쇠 열 수 있는지 확인
                if isOpen(arr, N):
                    return True
                # 배열 원상복구
                for k in range(M):
                    for l in range(M):
                        arr[i+k][j+l] -= key[k][l]
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))