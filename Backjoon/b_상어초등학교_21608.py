import sys 
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr = [[0]*n for _ in range(n)]
like_dict = defaultdict(list)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for _ in range(n*n):
    students = list(map(int, input().split()))
    like_dict[students[0]] = students[1:]

    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1

    for i in range(n):
        for j in range(n):
            # 비어 있는 자리면 카운트 시작, 모두 탐색
            if arr[i][j] == 0:
                like_cnt = 0
                empty_cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] == 0:
                            empty_cnt += 1
                        elif arr[nx][ny] in students:
                            like_cnt += 1
                
                if (max_like < like_cnt) or (max_like == like_cnt and max_empty < empty_cnt):
                    max_x = i
                    max_y = j
                    max_like = like_cnt
                    max_empty = empty_cnt
    # 최종적으로
    arr[max_x][max_y] = students[0]
answer = 0
for i in range(n):
    for j in range(n):
        like_friends = like_dict[arr[i][j]]
        tmp = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in like_friends:
                    tmp += 1
        if tmp <= 1:
            answer += tmp
        elif tmp == 2:
            answer += 10
        elif tmp == 3:
            answer += 100
        elif tmp == 4:
            answer += 1000
print(answer)