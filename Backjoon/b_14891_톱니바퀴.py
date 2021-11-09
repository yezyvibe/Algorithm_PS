from collections import deque

gear = [deque(map(int, input())) for _ in range(4)]
orders = deque(list(map(int, input().split())) for _ in range(int(input())))

while orders:
    num, d = orders.popleft()
    num -= 1 # 인덱스 맞춰주기
    tmp_2 = gear[num][2] # 2,6번자리 값 저장
    tmp_6 = gear[num][6]
    gear[num].rotate(d)
    tmp_direct = d

    # 시작 톱니의 왼쪽
    d = tmp_direct
    for i in range(num-1, -1, -1):
        if gear[i][2] != tmp_6:
            tmp_6 = gear[i][6]
            gear[i].rotate(d*-1)
            d *= -1
        else:
            break

    # 시작 톱니의 오른쪽
    d = tmp_direct
    for i in range(num+1, 4):
        if gear[i][6] != tmp_2:
            tmp_2 = gear[i][2]
            # 톱니 회전 후
            gear[i].rotate(d*-1)
            # 방향 바꾸기
            d *= -1
        else:
            break

# 점수 계산
result = 0
for i in range(4):
    if gear[i][0] == 1:
        result += 2**i
print(result)