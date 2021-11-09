def solution(files):
    idx = 0
    res_list = []
    original_list = []
    for name in files:
        num_cnt = 0 
        chk = 0
        tmp = ''
        tmp_list = []
        idx += 1
        original_list.append([idx, name])
        for i in name:
            if not chk and not i.isdigit():
                tmp += i
            elif i.isdigit():
                if not chk:
                    tmp_list.append(tmp)
                    tmp = ''
                    tmp += i
                    num_cnt += 1
                    chk = 1
                else:
                    tmp += i
                    num_cnt += 1
                    if num_cnt == 5:
                        chk = 2
                        while tmp[0] == '0':
                            tmp = tmp[1:]
                        tmp_list.append(tmp)
                        tmp_list.append(str(idx))
                        tmp = ''
            elif not i.isdigit() or chk == 2:
                if chk == 1 or chk == 2:
                    while tmp[0] == '0':
                        tmp = tmp[1:]
                    tmp_list.append(tmp)
                    tmp_list.append(str(idx))
                    tmp = ''
                    tmp += i
                    chk = 3
                else:
                    tmp += i
        else:
            if tmp.isdigit():
                tmp_list.append(tmp)
                tmp_list.append(idx)
                tmp_list.append('0')
            else:
                tmp_list.append(tmp)
    
        res_list.append(tmp_list)
    print(res_list)
    print(original_list)
    res_list.sort(key=lambda x:(x[0].lower(), int(x[1]), int(x[2]), x[3]))
    print(res_list)     
    
    answer = []
    for i in res_list:
        answer.append(original_list[int(i[2])-1][1])
    return answer

files = ["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))