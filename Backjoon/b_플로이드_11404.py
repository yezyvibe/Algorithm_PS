import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = float("inf")
arr = [[INF]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if arr[a-1][b-1] > c:
        arr[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                arr[i][j] = 0
                continue
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            print(0, end = " ")
        else:
            print(arr[i][j], end = " ")
    print()