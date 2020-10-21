import sys

input = sys.stdin.readline

rooms = []
for i in range(int(input())):
    a, b = map(int, input().split(' '))
    rooms.append([a, b])

rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
before = rooms[0][1]
cnt = 1
for room in rooms[1:]:
    s, e = room[0], room[1]
    if s >= before:
        cnt += 1
        before = e
print(cnt)
