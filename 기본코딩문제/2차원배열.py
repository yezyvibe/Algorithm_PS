n = int(input())
arr = [[0]*19 for i in range(19)]

for tc in range(n):
    dx, dy = list(map(int, input().split()))
    arr[dx-1][dy-1] = 1

for a in arr:
    print(' '.join(map(str, a)))
