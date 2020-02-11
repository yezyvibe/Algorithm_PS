arr = [list(map(int, input.split())) for i in range(10)]

locate_x = 1
locate_y = 1

while True:

    if arr[locate_x][locate_y+1] == 0:
        arr[locate_x][locate_y] = 9
        locate_y += 1
    elif arr[locate_x+1][locate_y] == 0:
        arr[locate_x][locate_y] = 9
        locate_x += 1


