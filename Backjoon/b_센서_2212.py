n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
dist = []
if k >= n:
    print(0)
else:
    for i in range(1, n):
        dist.append(sensor[i] - sensor[i-1])
    dist.sort()
    for i in range(k-1):
        dist.pop()
    print(sum(dist))    
