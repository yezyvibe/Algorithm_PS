import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if not n:
        break
    room = [[] for _ in range(n)]
    for i in range(n):
        tmp = list(input().rstrip().split())
        room[i].append(tmp[0])
        room[i].append(tmp[1])
        for j in range(2, len(tmp)-1):
            room[i].append(tmp[j])
    visit = [0]*n
    stack = [0]
    money = 0
    visit[0] = 1
    if room[0][0] == 'T':
        continue
    elif room[0][0] == 'L':
        money = room[0][1]

    while stack:
        x = stack.pop()
        for i in range(2, len(room[x])):
            idx = int(room[x][i]) - 1
            tmp = room[idx][0]
            if not visit[idx]:
                if tmp == 'L':
                    money = max(int(room[idx][1]), money)
                elif tmp == 'T':
                    money -= int(room[idx][1])
                if money >= 0:
                    stack.append(idx)
                    visit[idx] = 1
    if sum(visit) == n:
        print('Yes')
    else:
        print('No')
