import sys

def binary_search(x):
    start, end = 0, len(line) - 1
    while start <= end:
        mid = (start + end) // 2 
        if line[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1
    line[start] = x

input = sys.stdin.readline
n = int(input())
connect_info = list(map(int, input().split()))
line = []
for port in connect_info:
    if not line or line[-1] < port:
        line.append(port)
    else:
        binary_search(port)
print(len(line))