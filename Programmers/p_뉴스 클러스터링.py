from collections import Counter


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    lst1 = []
    lst2 = []

    # 유효한 두 글자씩 끊어서 리스트에 넣기
    for i in range(0, len(str1) - 1):
        tmp = str1[i:i + 2]
        if tmp.isalpha():
            lst1.append(tmp)
    for i in range(0, len(str2) - 1):
        tmp = str2[i:i + 2]
        if tmp.isalpha():
            lst2.append(tmp)

    # 모두 공집합인 경우
    if len(lst1) == len(lst2) == 0:
        return 65536

    # 교집합, 합집합의 길이 구해서 결과값 리턴
    c1 = Counter(lst1)
    c2 = Counter(lst2)
    inter = len(list((c1 & c2).elements()))
    union = len(list((c1 | c2).elements()))
    return int(inter / union * 65536)