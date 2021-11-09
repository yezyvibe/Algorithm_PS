import sys

input = sys.stdin.readline
n = int(input())
tower = list(map(int, input().rstrip().split(' ')))
res = [0] * n
s = []
for i in range(len(tower) - 1, -1, -1):
    while s and tower[s[-1]] < tower[i]:  # 탑 높이가 큰게 나오면
        res[s.pop()] = i + 1  # 수신하는 탑의 높이 저장
        # print(res, 'res')
    s.append(i)  # 위치 저장
print(*res)
