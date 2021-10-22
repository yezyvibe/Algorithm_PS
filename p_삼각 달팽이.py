def solution(n):
    arr = [[0]*n for _ in range(n)]
    answer = []
    x, y = -1, 0  # 행, 열
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:   # down
                x += 1
            elif i % 3 == 1:   # right
                y += 1
            elif i % 3 == 2:   # left
                x -= 1
                y -= 1

            arr[x][y] = num
            num += 1
    
    for a in arr:
        for item in a:
            if item:
                answer.append(item)
    return answer



print(solution(4))