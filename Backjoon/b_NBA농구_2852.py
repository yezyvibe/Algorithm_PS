import sys
from collections import defaultdict


input = sys.stdin.readline
winning_time = defaultdict(list)
before = [0,0]
for i in range(int(input())):
    team, time = map(str, input().split())
    time = time.split(':')
    m = int(time[0])-before[0]
    s = int(time[1])-before[1]
    if team not in winning_time:
        winning_time[team] = [m, s]
    else:
        winning_time[team][0] += m
        winning_time[team][1] += s
    before[0], before[1] = int(time[0]), int(time[1])
    print(winning_time)
print(f'끝 {winning_time}')