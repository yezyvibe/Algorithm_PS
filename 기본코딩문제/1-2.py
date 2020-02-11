T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(n)]

print(arr)