def solution(n, m, x, y, queries):
    x_min, x_max, y_min, y_max = x, x, y, y

    for i in range(len(queries)-1, -1, -1):
        k, dx = queries[i]
        if k == 0: # 열 번호 감소
            y_max += dx
            if y_max > m - 1:
                y_max = m - 1
            if y_min != 0:
                y_min += dx

        elif k == 1: # 열 번호 증가
            y_min -= dx
            if y_min < 0:
                y_min = 0
            if y_max != m - 1:
                y_max -= dx
    
        elif k == 2: # 행 번호 감소
            x_max += dx
            if x_max > n - 1:
                x_max = n - 1
            if x_min != 0:
                x_min += dx
            
        elif k == 3: # 행 번호 증가
            x_min -= dx
            if x_min < 0:
                x_min = 0
            if x_max != n - 1:
                x_max -= dx

        if y_min > m - 1 or y_max < 0 or x_min > n-1 or x_max < 0:
            return 0
    return (y_max - y_min + 1) * (x_max - x_min + 1)

print(solution(	2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))