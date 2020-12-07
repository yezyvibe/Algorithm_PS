import sys

# i는 행 인덱스
def dfs(i):
    global n, col, cross_left, cross_right, answer

    if i == n:
        answer += 1
        return
    for j in range(n):
        if not(col[j] or cross_right[i+j] or cross_left[i-j+n-1]):
            col[j] = cross_right[i+j] = cross_left[i-j+n-1] = 1
            dfs(i+1)
            col[j] = cross_right[i+j] = cross_left[i-j+n-1] = 0


input = sys.stdin.readline
n = int(input())
col = [0]*n
cross_left = [0]*(2*n-1)
cross_right = [0]*(2*n-1)
answer = 0
dfs(0)
print(answer)