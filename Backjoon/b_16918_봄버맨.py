import sys
from copy import deepcopy


def bomb(arr, bomb_list):
    global zero_arr
    copy_arr = deepcopy(zero_arr)
    d = [(-1,0), (1, 0), (0, -1), (0, 1)]   # 상하좌우
    for x, y in bomb_list:
        copy_arr[x][y] = '.'     
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                copy_arr[nx][ny] ='.'

    return copy_arr



input = sys.stdin.readline
r, c, n = map(int, input().split())

zero_arr = [['O']*c for _ in range(r)]
arr = []
for i in range(r):
    arr.append(list(input().rstrip()))

time = 1
chk = 1
while time < n:
    if chk:
        time += 1
        chk = 0
        continue
    elif not chk:
        time += 1
        chk = 1
        bomb_list = []  
        for i in range(r):
            for j in range(c):
                if arr[i][j] == 'O':
                    bomb_list.append((i, j))
        else:
            arr = deepcopy(bomb(arr, bomb_list))
if not chk:
    for a in zero_arr:
        print(''.join(a))
else:
    for a in arr:
        print(''.join(a))          
    
