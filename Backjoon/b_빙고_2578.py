import numbers
import sys 

def findIndex(num):
    for i in range(5):
        for j in range(5):
            if cheolsu[i][j] == num:
                cheolsu[i][j] = -1
def findBingo():
    cnt = 0
    # 가로줄 확인
    for i in range(5):
        for num in cheolsu[i]:
            if num != -1:
                break
        else:
            cnt += 1
    # 세로줄 확인
    for j in range(5):
        for i in range(5):
            if cheolsu[i][j] != -1:
                break
        else:
            cnt += 1
    # 대각선 확인
    for i in range(5):
        if cheolsu[i][i] != -1:
            break
    else:
        cnt += 1
    
    for i in range(5):
        if cheolsu[i][5 -i -1] != -1:
            break
    else:
        cnt += 1

    return cnt

input = sys.stdin.readline
cheolsu = [list(map(int, input().split())) for _ in range(5)]
moderator = [list(map(int, input().split())) for _ in range(5)]
answer = 0
for i in range(5):
    for j in range(5):
        answer += 1
        num = moderator[i][j]
        findIndex(num)
        if findBingo() >= 3:
            print(answer)
            exit(0)
