# 정확성만 맞춘 풀이
def solution(board, skill):

    for i in range(len(skill)):
        type, r1, c1, r2, c2, degree = skill[i]

        if type == 1:
            degree = - degree

        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                board[j][k] += degree

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    
    return answer


# 정확성, 효율성 모두 고려한 풀이

def solution(board, skill):
    n = len(board) # 세로
    m = len(board[0]) # 가로
    arr = [[0] * (m+1) for _ in range(n+1)]

    for i in range(len(skill)):
        type, r1, c1, r2, c2, degree = skill[i]
        if type == 1:
            degree = - degree
        arr[r1][c1] += degree
        arr[r2+1][c1] -= degree
        arr[r1][c2+1] -= degree
        arr[r2+1][c2+1] += degree

    for i in range(1, n+1):
        for j in range(m+1):
            arr[i][j] += arr[i-1][j]


    for i in range(1, m+1):
        for j in range(n+1):
            arr[j][i] += arr[j][i-1]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))