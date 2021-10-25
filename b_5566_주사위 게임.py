import sys

input = sys.stdin.readline
n, m = map(int, input().split())
game_map = [int(input()) for _ in range(n)]
sangkuen = 0
for i in range(m):
    dice = int(input())
    sangkuen += dice
    # print(f'dice: {dice}', f'sang:{sangkuen}')
    if sangkuen >= (n-1):
        print(i+1)
        break
    if game_map[sangkuen]:
        sangkuen += game_map[sangkuen]
        # print(f'sang:{sangkuen}')
    if sangkuen >= (n-1):
        print(i+1)
        break
else:
    print(m)
