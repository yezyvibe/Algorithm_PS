import sys

def count_color():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
    return max_cnt



input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
answer = 1
for i in range(n):
    for j in range(1, n):
        # 같은 행 오른쪽 사탕과 교환(index주의)
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        answer = max(answer, count_color())
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        # 같은 열 위쪽 사탕과 교환(index주의)
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
        answer = max(answer, count_color())
        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]

print(answer)

