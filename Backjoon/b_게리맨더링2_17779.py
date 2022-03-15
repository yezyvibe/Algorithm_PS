import sys


def boundary(n, x, y, d1, d2, bg):
    arr = [[0]*(n+1) for _ in range(n+1)]
    people = [0] * 5
    # 5번 선거구 표시하기
    arr[x][y] = 5
    for i in range(1, d1 + 1):
        arr[x + i][y - i] = 5

    for i in range(1, d2+1):
        arr[x + i][y + i] = 5

    for i in range(1, d2 + 1):
        arr[x + d1 + i][y - d1 + i] = 5

    for i in range(1, d1 + 1):
        arr[x + d2 + i][y + d2 - i] = 5


    for i in range(1, x+d1):
        for j in range(1, y+1):
            if arr[i][j] == 5:
                break
            people[0] += bg[i][j]

    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if arr[i][j] == 5:
                break
            people[1] += bg[i][j]         

    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if arr[i][j] == 5:
                break
            people[2] += bg[i][j]  

    for i in range(x+d2 +1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if arr[i][j] == 5:
                break
            people[3] += bg[i][j]  

    people[4] = total - sum(people)
    return max(people) - min(people)


# 시뮬레이션 -> 단계별로 주석 달면서 꼼꼼하게 풀기
input = sys.stdin.readline
n = int(input())
bg = [[0]*(n + 1)] + [[0] +list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(1, n+1):
    total += sum(bg[i])

answer = float('inf')
# 1단계 범위를 만족하는 경우만 탐색 시작
for  x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    answer = min(answer, boundary(n, x, y, d1, d2, bg))
                    
print(answer)