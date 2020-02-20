t = int(input())
for tc in range(1,t+1):
    n , k = map(int,input().split())
    arr = [list(map(int,input().split())) for l in range(n)]
    score = []
    for i in range(n):

        arr[i][0] = (arr[i][0])*0.35
        arr[i][1] = (arr[i][1])*0.45
        arr[i][2] = (arr[i][2])*0.20
        score_sum = arr[i][0] + arr[i][1] + arr[i][2]
        score.append(score_sum)
    score.sort()
    score.reverse()
    res = score[k-1]
    # print(res)

for j in range(0,n,(n//10)):
