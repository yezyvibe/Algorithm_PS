import math

def solution(n, clockwise):
    # n x n 배열 만들기
    arr = [[0] * n for _ in range(n)]
    # 돌아가는 횟수
    length = math.ceil(n / 2)
    # 시작점
    start_points = [(0, 0), (0, n-1), (n-1, n-1), (n-1, 0)]
    
    max_v = n - 1
    cnt = 2
    x, y = n -1, n-1
    for i in range(length):
        if cnt == 0: # 좌 -> 우 , x 고정
            for j in range(max_v):
                print(x, y + j)
            max_v -= 1
            y = max_v # 다 끝나고 y 고정시키기
        elif cnt == 1: # 상 -> 하 , y 고정
            for j in range(max_v):
                print(j, y)
            max_v -= 1
            x = max_v # 다 끝나고 x 고정시키기
        elif cnt == 2: # 좌 -> 우 , x 고정
            print('cnt', cnt)
            for j in range(max_v):
                print(x, y - j)
            max_v -= 1
            y =  y - j
        
        elif cnt == 3: # 하 -> 상 , y 고정
            print('cnt', cnt)
            for j in range(max_v):
                print(x- j, y)
        cnt += 1
        if cnt == 4:
            cnt = 0
        print("끝")

print(solution(5, True))
