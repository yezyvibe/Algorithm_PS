# arr = [list(map(int, input().split())) for l in range(4)]
# square_list = []
# for k in range(4):
#     x1,y1,x2,y2 = map(int,input().split())
#     square = (x2-x1)*(y2-y1)
#     print(square)
#     square_list.append(square)
# print(square_list)


# 겹치는 부분을 없애줘야 함
# 이렇게 풀면 안 될 거 같음 for문 돌려서 해당 행열에 1씩 더해주기
# if 문 돌려서 이미 1이 있는 경우에는 넣지 않기

arr = [[0]*100 for l in range(100)]

for k in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2 - x1):
        for j in range(y2 - y1):
            if arr[x1 + i][y1 + j] == 0:
                arr[x1 + i][y1 + j] = 1
            elif arr[x1 + i][y1 + j] == 1:
                arr[x1 + i][y1 + j] = 1

square_cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            square_cnt += 1
            arr[i][j] = square_cnt
print(square_cnt)



