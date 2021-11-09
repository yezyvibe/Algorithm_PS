from itertools import combinations as combi

def solution(line):
    n_list = [i for i in range(len(line))]
    start_points = []
    x_list, y_list = [], []

    # 별을 찍는 위치 구하기
    for i, j in combi(n_list, 2):
        a, b, e = line[i]
        c, d, f = line[j]
        if (a*d - b*c):
            x = (b*f - e*d) / (a*d - b*c)
            y = (e*c - a*f) / (a*d - b*c)
            if x.is_integer() and y.is_integer():
                start_points.append((int(x), int(y)))
                x_list.append(int(x))
                y_list.append(int(y))

    # x, y의 최대 최솟값과 배열의 크기 구하기
    max_x, min_x = max(x_list), min(x_list)
    max_y, min_y = max(y_list), min(y_list)
    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1

    # 수학적 좌표평면의 위치를(4분면 영역이 있는) -> 컴퓨터의 좌표순서(1사분면만 존재하게)로 바꿔주기 
    arr = [['.'] * x_size for _ in range(y_size)]
    for x, y in start_points:
        arr[max_y-y][-min_x+x] = '*'

    return [''.join(s) for s in arr]

line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
print(solution(line))