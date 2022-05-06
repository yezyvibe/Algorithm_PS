def get_point(round, info, n):
    arrow = n
    for i in range(len(round)):
        if round[i] == "1": # 점수를 획득한 경우
            arrow -= (int(info[i]) + 1)
            if arrow < 0:
                return 0

    apichi = 0
    lion = 0
    for i in range(len(info)):
        if i < len(round) and round[i] == "1":
            lion += (10 - i)
        elif int(info[i]):
            apichi += (10 - i)
    return lion - apichi if lion > apichi else 0 




def solution(n, info):
    answer = []
    max_v = -1
    round = ""
    next = ["0", "1"]
    info = "".join(map(str, info))

    def dfs(round, n, info):
        nonlocal answer, max_v
        if len(round) == 11:
            return
        for item in next:
            result = get_point(round + item, info, n) 
            if result:
                if result > max_v :
                    max_v = result
                    answer = [round + item]
                    # print(answer, "1qqqqqqqqqq","최솟값:",  max_v)
                elif result == max_v:
                    answer.append(round + item)
                    # print(answer, "2qqqqqqq","최솟값:",  max_v)
            dfs(round + item, n, info)
    
    dfs(round, n, info)
    answer = [i  for i in answer if len(i) == 11]
    if not answer:
        return [-1]
    
    for i in range(10, -1, -1):
        tmp = []
        for j in range(len(answer)):
            if int(answer[j][i]):
                tmp.append([j, i, answer[j][i]])
        if tmp:
            tmp.sort(key=lambda x :x[2])
            res = answer[tmp[-1][0]]
            break    

    final = []
    for i in range(11):
        if res[i] == "1":
            final.append(int(info[i]) + 1)
        else:
            final.append(0)
    final_sum = sum(final)
    if final_sum < n:
        final[-1] += (n - final_sum)
    return final

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))
