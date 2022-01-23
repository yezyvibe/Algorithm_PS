from abc import ABCMeta
import sys

input = sys.stdin.readline
a, b, c = map(int, input().rstrip().split(' '))
time_table = [0]*101
for i in range(3):
    arrive, depart = map(int, input().rstrip().split(' '))
    for j in range(arrive-1,depart-1):
        time_table[j] += 1
answer = 0
for k in time_table:
    if k == 1:
        answer += a*k
    elif k == 2:
        answer += b*k
    elif k == 3:
        answer += c*k
print(answer)