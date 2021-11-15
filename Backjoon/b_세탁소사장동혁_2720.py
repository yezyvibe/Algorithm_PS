import sys

input = sys.stdin.readline
coin = [25, 10, 5, 1]
for i in range(int(input())):
    change = int(input())
    answer = [0, 0, 0, 0]
    for j in range(4):
        if coin[j] <= change:
            q, r = divmod(change, coin[j])
            answer[j] = q
            change = r
    print(' '.join(map(str, answer)))