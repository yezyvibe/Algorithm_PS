import sys
import heapq

input = sys.stdin.readline
time_table = []
for i in range(int(input())):
    s, e = map(int, input().split())
    heapq.heappush(time_table, [s, e])

s, e = heapq.heappop(time_table)
room = [e]

for i in range(len(time_table)):
    s, e = heapq.heappop(time_table)
    if room[0] <= s:   # 가장 수업이 빨리 끝나는 강의실의 끝나는 시간과 다음 강의실의 시작 시간을 비교
        heapq.heappop(room)
        heapq.heappush(room, e)
    else:
        heapq.heappush(room, e)
print(len(room))