def solution(arr):
    n = len(arr)
    answer = [0, 0]
    
    def compression(x, y, n):
        start = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != start:
                    n = n // 2
                    compression(x, y, n)
                    compression(x+n, y, n)
                    compression(x, y+n, n)
                    compression(x+n, y+n, n)
                    return
        answer[start] += 1
    
    compression(0, 0, n)
    return answer