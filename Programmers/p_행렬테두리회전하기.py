def solution(rows, columns, queries):
    arr = [[0]*columns for _ in range(rows)]
    num = 1
    answer = []
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = num
            num += 1
    
    for a,b,c,d in queries:
        before = arr[a-1][b-1]
        min_value = 10000
        for j in range(b, d):
            min_value = min(before, min_value)
            before, arr[a-1][j] = arr[a-1][j], before
        for i in range(a, c):
            min_value = min(before, min_value)
            before, arr[i][d-1] = arr[i][d-1], before
        for j in range(d-2, b-2, -1):
            min_value = min(before, min_value)
            before, arr[c-1][j] = arr[c-1][j], before
        for i in range(c-2, a-2, -1):
            min_value = min(before, min_value)
            before, arr[i][b-1] = arr[i][b-1], before
        answer.append(min_value)
    
    return answer
        

        


rows, columns = 3, 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, queries))
