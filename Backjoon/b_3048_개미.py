import sys


input = sys.stdin.readline
n, m = map(int, input().split())
group1, group2 = list(input().rstrip()), list(input().rstrip())
time = int(input())
dir = {}
for ant in group1:
    dir[ant] = 0   # 뒤로 이동
for ant in group2:
    dir[ant] = 1   # 앞으로 이동

group1.reverse()
group1.extend(group2)

for i in range(time):
    index = 0
    while index < len(group1) -1:
        if dir[group1[index]] == 0 and dir[group1[index+1]] == 1:
            group1[index], group1[index+1] = group1[index+1], group1[index]
            index += 1
        index += 1
print(''.join(map(str, group1)))
 