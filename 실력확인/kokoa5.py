def solution(commands):
    # 병합된 행렬인지 확인하는 행렬 두기(행렬 해당 위치가 병합된 것인지 확인하는 행렬)
    arr = [[0]*51 for _ in range(51)]
    check_arr = [[0]*51 for _ in range(51)]
    chk_cnt = 1
    answer = []
    for k in range(len(commands)):
        cur = commands[k].split(" ")
        command = cur[0]
        
        # 1 
        if command == 'UPDATE' and len(cur) == 4:
            r, c, value = int(cur[1]), int(cur[2]), cur[3]
            arr[r][c] = value
            for i in range(51):
                for j in range(51):
                    if check_arr[i][j] == check_arr[r][c] and check_arr[r][c]:
                        arr[i][j] = value
            continue
        
        # 2
        if command == 'UPDATE' and len(cur) == 3:
            value1, value2 = cur[1], cur[2]
            for i in range(51):
                for j in range(51):
                    if arr[i][j] == value1:
                        arr[i][j] = value2
            continue
        # 3
        if command == 'MERGE':
            r1, c1, r2, c2 = int(cur[1]), int(cur[2]), int(cur[3]), int(cur[4])
            value1 = arr[r1][c1]
            value2 = arr[r2][c2]

            # 병합을 먼저 하고 그 다음 값을 하나로 바꿔주기
            if check_arr[r1][c1]:
                tmp = check_arr[r1][c1]
                for i in range(51):
                    for j in range(51):
                        if check_arr[i][j] == tmp:
                            check_arr[i][j] = chk_cnt
            if check_arr[r2][c2]:
                tmp = check_arr[r2][c2]
                for i in range(51):
                    for j in range(51):
                        if check_arr[i][j] == tmp:
                            check_arr[i][j] = chk_cnt
            check_arr[r1][c1] = chk_cnt
            check_arr[r2][c2] = chk_cnt

            if value1:
                for i in range(51):
                    for j in range(51):
                        if check_arr[i][j] == chk_cnt:
                            arr[i][j] = value1
            elif not value1 and value2:
                for i in range(51):
                    for j in range(51):
                        if check_arr[i][j] == chk_cnt:
                            arr[i][j] = value2
            
            chk_cnt += 1
            continue
        # 4
        if command == 'UNMERGE':
            r, c = int(cur[1]), int(cur[2])
            before_value = arr[r][c]
            tmp = check_arr[r][c]
            for i in range(51):
                for j in range(51):
                    if tmp and check_arr[i][j] == tmp:
                        # 병합 풀기 -> 초기화
                        check_arr[i][j] = 0
                        arr[i][j] = 0
            arr[r][c] = before_value
            continue
        # 5
        if command == 'PRINT':
            r, c = int(cur[1]), int(cur[2])
            if arr[r][c]:
                answer.append(arr[r][c])
            else:
                answer.append('EMPTY')

    return answer



commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))