import sys

def convert(arr_a, i, j):
    for k in range(i, i+3):
        for l in range(j, j+3):
            if arr_a[k][l] == 0:
                arr_a[k][l] = 1
            else:
                arr_a[k][l] = 0


input = sys.stdin.readline
n, m = map(int, input().split())
arr_a = [list(map(int, input().rstrip())) for _ in range(n)]
arr_b = [list(map(int, input().rstrip())) for _ in range(n)]
answer = 0
for i in range(n-2):
    for j in range(m-2):
        if arr_a[i][j] != arr_b[i][j]:
            convert(arr_a, i, j)
            answer += 1
 

for i in range(n):
    for j in range(m):
        if arr_a[i][j] != arr_b[i][j]:
            answer = -1
            break
    if answer == -1:
        break
print(answer)



