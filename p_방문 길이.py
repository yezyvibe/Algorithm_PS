def solution(dirs):
    arr = [[0]*11 for _ in range(11)]
    dict = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    x, y = 5, 5
    cnt = 0
    check = set()
    for dir in dirs:
        print(dir)
        a, b = dict[dir]
        nx, ny = x+a, y+b
        if 0 <= nx < 11 and 0<= ny < 11:
            if (nx, ny, x, y) not in check or (x, y, nx, ny) not in check:
                cnt += 1
                check.add((nx, ny, x, y))
                check.add((x, y, nx, ny))
                print(check)
            x, y = nx, ny # 이동을 나타내기 위해 x, y값 업데이트
                
    for a in arr:
        print(a)        
    return cnt

dirs = "UDU" 
print(solution(dirs))
