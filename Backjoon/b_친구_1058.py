import sys

input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
friends = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or friends[i][j]:
                continue
            if arr[i][j] == "Y":
                friends[i][j] = 1
                friends[j][i] = 1
                continue
            if arr[k][i] == arr[k][j] == "Y":
                friends[i][j] = 1
                friends[j][i] = 1
                continue
max_v = 0
for i in friends:
    max_v = max(sum(i), max_v)
print(max_v)