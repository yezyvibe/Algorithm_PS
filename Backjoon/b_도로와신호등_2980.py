import sys

input = sys.stdin.readline
n, l = map(int, input().rstrip().split())
answer = 0
current = 0
for i in range(n):
    d, r, g = map(int, input().rstrip().split())
    answer += (d-current)
    current = d
    if answer % (r+g) <= r:
        answer += (r - (answer % (r+g)))
answer += (l-current)
print(answer)