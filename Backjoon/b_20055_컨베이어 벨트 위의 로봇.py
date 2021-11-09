import sys
from collections import deque


input = sys.stdin.readline
n, k = map(int, input().split())
conveyor_belt = deque(list(map(int, input().split())))
robot = deque([0]*n)
answer = 0

while True:
    robot.rotate(1)
    conveyor_belt.rotate(1)
    robot[-1] = 0
    
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and conveyor_belt[i+1]:
            conveyor_belt[i+1] -= 1
            robot[i+1] = 1
            robot[i] = 0
    robot[-1] = 0

    if not robot[0] and conveyor_belt[0] > 0:
        robot[0] = 1
        conveyor_belt[0] -= 1
        
    answer += 1
    if conveyor_belt.count(0) >= k:
        break
print(answer)
