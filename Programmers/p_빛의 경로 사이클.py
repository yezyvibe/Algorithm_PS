from collections import defaultdict

def solution(grid):
    answer = []
    grid = list(map(lambda x : list(x), grid))
    # print(grid)
    n, m = len(grid), len(grid[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 하 우 상 좌
    dic = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in d:
                if k not in dic[(i, j)]:  # i.j 좌표에 해당 방향이 없다면
                    d1, d2 = k
                    x, y = i, j
                    result = 0
                    
                    while (d1, d2) not in dic[(x, y)]:
                        result += 1
                        dic[(x, y)].append((d1, d2))
                        x += d1   # 이동 후
                        y += d2
                        
                        # 범위 넘어가는 경우 처리
                        if x == -1: x = n - 1  # 맨 위 넘어가면 제일 아래로 이동
                        if x == n: x = 0  # 맨 아래 넘어가면 제일 위로 이동
                        if y == -1: y = m - 1  # 맨 왼쪽 넘어가는 경우 제일 오른쪽으로 이동  
                        if y == m: y = 0  # 맨 오른쪽 넘어가는 경우 제일 왼쪽으로 이동

                        s = grid[x][y]
                        if s == 'L': d1, d2 = (d2, d1) if d1 != 0 else (-d2, -d1)
                        if s == 'R': d1, d2 = (-d2, -d1) if d1 != 0 else (d2, d1)

                    answer.append(result)

    answer.sort()
    return answer

print(solution(['SL', 'LR'])) 