import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def check(x, y, n, number):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != number:
                # 종이 못 만드니까 쪼개야 한다
                return False

    return True

answer = defaultdict(int)

def dfs(x, y, n):
    if not check(x, y, n, arr[x][y]):
        # 삼등분하기
        for k in range(3):
            for l in range(3):
                dfs(x+k*n//3, y+l*n//3, n//3)
        return

    else:
        answer[arr[x][y]] += 1

dfs(0, 0, n)

for i in [-1, 0, 1]:
    print(answer[i])

