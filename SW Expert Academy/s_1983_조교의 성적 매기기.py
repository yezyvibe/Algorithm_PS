t = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']
for tc in range(1,t+1):
    n , k = map(int,input().split())
    arr = [list(map(int,input().split())) for l in range(n)]
    score = []
    grade_dic = {}
    for i in range(n):

        arr[i][0] = (arr[i][0])*0.35
        arr[i][1] = (arr[i][1])*0.45
        arr[i][2] = (arr[i][2])*0.20
        score_sum = arr[i][0] + arr[i][1] + arr[i][2]
        score.append(score_sum)
    temp_score = sorted(score)
    temp_score.reverse()
    temp_dic = {}

    cnt = 0
    for j in range(1, n+1):
        temp_dic[temp_score[j-1]] = grade[cnt]

        if j % (n/10) == 0:
            cnt += 1
    for idx, sco in enumerate(score):
        grade_dic[idx+1] = temp_dic[sco]
    print('#{} {}'.format(tc, grade_dic[k]))
