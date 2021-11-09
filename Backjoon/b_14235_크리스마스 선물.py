import sys
import heapq

input = sys.stdin.readline
present = []
for i in range(int(input())):
    a = input().rstrip().split(' ')
    # print('a:', a)
    if a[0] == '0':
        try:
            p = heapq.heappop(present)
            print(-p)
        except:
            print(-1)
    else:
        a = list(map(int, a))
        for k in range(a[0]):
            heapq.heappush(present, -a[k+1])
