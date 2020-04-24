import sys

def search(idx, cnt):
    global res
    if idx > len(chicken):
        return
    if cnt == m:
        city_total = 0
        for x1, y1 in house:
            distance = 10000000
            for i in visit:
                x2, y2 = chicken[i]
                distance = min(distance, abs(x1 - x2) + abs(y1 - y2))
            city_total += distance
        res = min(res, city_total)
        return
    visit.append(idx)
    search(idx+1, cnt+1)
    visit.pop()
    search(idx+1, cnt)


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 10000000
house = []
chicken = []
visit = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))
search(0, 0)
print(res)
