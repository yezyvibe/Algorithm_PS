
# t = int(input)
# cnt = 0

 # for time in range(1, t+1):
 #     if x < w and y < h:
 #            x = x + 1
 #    elif x == w or y == h:

# (4,1) (5,3)

w, h = list(map(int, input().split()))
x, y = list(map(int, input().split()))
t = int(input())
dx = [1, -1, -1, -1]
dy = [1, 1, -1, 1]
mode = 0


def iswall(tx, ty):
    if tx == w or ty ==h :
        return False
    else:
        return True
for i in range(t):
    while not iswall(x+dx[mode], y+dy[mode]):
        mode = (mode + 1) % 4

    x += dx[mode]
    y += dx[mode]




