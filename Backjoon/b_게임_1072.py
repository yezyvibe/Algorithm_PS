from math import floor
import sys


input = sys.stdin.readline
x, y = map(int, input().split())
z = floor(y / x)  * 100
start, end = 0, 1000000000

if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        tmp = floor((mid+y)*100/(mid+x))
        
        if tmp > z:
            end = mid - 1
        else:
            start = mid + 1
    print(start)