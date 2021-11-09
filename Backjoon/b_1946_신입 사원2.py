import sys

input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    rank = [tuple(map(int, input().split(' '))) for _ in range(n)]
    rank.sort(key=lambda x: x[0])
    max_v = 100001
    cnt = 0
    for i in range(n):
        if rank[i][1] < max_v:
            max_v = rank[i][1]
            cnt += 1
    print(cnt)