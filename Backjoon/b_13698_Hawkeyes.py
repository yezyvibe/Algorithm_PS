import sys

input = sys.stdin.readline
ball_list = ['small', 0, 0, 'big']
for order in input():
    if order == 'A':
        ball_list[0], ball_list[1] = ball_list[1], ball_list[0]
    elif order == 'B':
        ball_list[0], ball_list[2] = ball_list[2], ball_list[0]
    elif order == 'C':
        ball_list[0], ball_list[3] = ball_list[3], ball_list[0]
    elif order == 'D':
        ball_list[1], ball_list[2] = ball_list[2], ball_list[1]
    elif order == 'E':
        ball_list[1], ball_list[3] = ball_list[3], ball_list[1]
    elif order == 'F':
        ball_list[2], ball_list[3] = ball_list[3], ball_list[2]

print(ball_list.index('small')+1)
print(ball_list.index('big')+1)
