import math


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    set1, set2 = [], []
    
    if str1 == str2:
        return 65536
    
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            set1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            set2.append(str2[i:i+2])

    intersection = 0
    for i in range(len(set1)):
        for j in range(len(set2)):
            if set1[i][0] == set2[j][0]:
                if set1[i] == set2[j]:
                    intersection += 1
                    print(set1[i], set2[j], intersection)
                    set2.remove(set1[i])
                    break

    union = len(set1) + len(set2)
    answer = math.floor((intersection/union) * 65536)
    return answer