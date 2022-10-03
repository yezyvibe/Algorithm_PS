import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(triangle[i])):
        left, right = 0, 0
        if 0 <= j - 1:
            left = triangle[i-1][j-1] # 왼쪽 위
        if j < len(triangle[i]) - 1:
            right = triangle[i-1][j] # 오른쪽 위
        triangle[i][j] += max(left, right)

print(max(triangle[n-1]))