answer = 100000000
for slicing in range(1, len(s)//2+1):
    res = ''
    cnt = 1
    tmp = s[:slicing]

    for i in range(slicing, len(s)+slicing, slicing):
        if tmp == s[i:i+slicing]:
            cnt += 1
        else:
            if cnt == 1:
                res += s[i:i+slicing]
            else:
                res = res + str(cnt) + s[i:i+slicing]
            tmp = s[i:i+slicing]
            cnt = 1
    answer = min(answer, len(res))
return answer