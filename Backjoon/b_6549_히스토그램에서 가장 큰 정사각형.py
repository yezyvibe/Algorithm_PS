import sys

input = sys.stdin.readline
while True:
    arr = list(map(int, input().rstrip().split(' ')))
    arr.append(0)  # 전체 너비 맞춰주기
    if arr[0] == 0:
        break
    arr = arr[1:]
    s = []  # 비교대상인 이전 인덱스 저장
    max_v = 0
    for i, h in enumerate(arr):
        print(i, h)
        while s and arr[s[-1]] > h:  # 인덱스 이전값들의 높이 확인
            height = arr[s.pop()]  # 나보다 큰 애들을 기준으로 height 업데이트
            # print('height:', height)
            w = i - s[-1] - 1 if s else i  # 너비 계산
            # print('w:', w)
            if max_v < w * height:
                max_v = w * height
        s.append(i)
        # print('s:', s)
    print(max_v)
