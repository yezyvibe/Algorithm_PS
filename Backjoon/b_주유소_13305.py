import sys

input = sys.stdin.readline
n = int(input())
road_length = list(map(int, input().rstrip().split()))
oil_price = list(map(int, input().rstrip().split()))
min_v = oil_price[0]
answer = 0
for i in range(n-1):
    if oil_price[i] < min_v:
        min_v = oil_price[i]
    answer += road_length[i] * min_v
print(answer)