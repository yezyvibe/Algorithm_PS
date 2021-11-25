import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

answer = 0
for i in range(n-1, -1, -1):    # 큰 값의 동전부터 나누어본다
    answer += (k // coin[i])
    k = k % coin[i]

print(answer)

