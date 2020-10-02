def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] = max(land[i][1:4]) + land[i+1][0]
        land[i+1][1] = max(land[i][0], max(land[i][2:4])) + land[i+1][1]
        land[i+1][2] = max(max(land[i][0:2]), land[i][3]) + land[i+1][2]
        land[i+1][3] = max(land[i][0:3]) + land[i+1][3]
    return max(land[-1])