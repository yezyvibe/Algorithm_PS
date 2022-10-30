def solution(n, m, x, y, r, c, k):
    arr = [['.'] *(m) for _ in range(n)]
    arr[x-1][y-1] = 's'
    arr[r-1][c-1] = 'e'
    dx, dy, chars = [-1, 1, 0, 0], [0, 0, -1, 1], ['u', 'd', 'l', 'r']
    answer = []

    def dfs(a, b, res):
        L = len(res)
        # print(a,b,res,arr[a-1][b-1])
        if L == k and arr[a][b] == 'e':
            answer.append(res)
        if L < k:
            for i in range(4):
                na, nb = a + dx[i], b + dy[i]
                if 0 <= na < n and 0 <= nb < m:
                    dfs(na, nb, res + chars[i])
                    
    dfs(x-1, y-1, '')
    answer.sort()
    return answer[0] if answer[0] else 'impossible'
print(solution(3, 4, 2, 3, 3, 1, 5))