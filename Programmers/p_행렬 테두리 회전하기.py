def solution(rows, columns, queries):
    arr = [[0]*columns for _ in range(rows)]
    cnt = 1
    result = []

    for i in range(rows):
        for j in range(columns):
            arr[i][j] = cnt
            cnt += 1

    for r1, c1, r2, c2 in queries:
        min_v = 10001
        before = arr[r1][c1-1]

        # 위
        for i in range(c1-1, c2):
            min_v = min(arr[r1-1][i], min_v)
            before, arr[r1-1][i] = arr[r1-1][i], before

        # 오른쪽
        for i in range(r1, r2):
            min_v = min(arr[i][c2-1], min_v)
            before, arr[i][c2-1] = arr[i][c2-1], before  
            
        # 아래
        for i in range(c2-2, c1-2, -1):
            min_v = min(arr[r2-1][i], min_v)
            before, arr[r2-1][i] = arr[r2-1][i], before
            
        # 왼쪽
        for i in range(r2-2, r1-1, -1):
            min_v = min(arr[i][c1-1], min_v)
            before, arr[i][c1-1] = arr[i][c1-1], before
    
        result.append(min_v)
    return result