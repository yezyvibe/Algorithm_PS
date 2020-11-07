def solution(arr):
    new_len = len(arr)  # 전체 길이
    origin_len = len(arr)
    res = [0, 0]
    while new_len != 0:
        for i in range(0, origin_len, new_len):
            for j in range(0, origin_len, new_len):
                start = arr[i][j]
                chk = 0
                for k in range(i, i + new_len):
                    for l in range(j, j + new_len):
                        if arr[k][l] != start or arr[k][l] == 3:
                            chk = 1
                            break
                    if chk == 1:
                        break
                else:
                    res[start] += 1
                    for k in range(i, i + new_len):
                        for l in range(j, j + new_len):
                            arr[k][l] = 3
        new_len //= 2
    return res