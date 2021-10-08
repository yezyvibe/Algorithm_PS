def solution(s):
    answer = []
    res = ""
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        tmp_s, cnt = "", 1
        for j in range(0, len(s), i):
            if j == 0:
                tmp_s = s[j:j+i]
            else:
                if s[j:j+i] == tmp_s:
                    cnt += 1
                else:
                    if cnt == 1:
                        res += tmp_s
                    else:
                        res += (str(cnt) + tmp_s)
                    cnt = 1
                    tmp_s = s[j:j+i]

        else:
            if cnt == 1:
                res += tmp_s
            else:
                res += (str(cnt) + tmp_s)
            answer.append(len(res))
            res = ""

    return min(answer)


s = "a"
print(solution(s))