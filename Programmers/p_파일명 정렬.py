def solution(files):
    # 아래 f_name에다가 head, number, 전체문자열, 인덱스(몇 번째 파일인지) 순으로 데이터저장
    f_name = [[''] * 4 for _ in range(len(files))]
    idx = 0

    for file in files:
        # 파일 하나씩 꺼내서
        chk = 0
        num_cnt = 0
        f_name[idx][2] = file  # 전체 파일명 우선 저장하고

        for i in range(len(file)):  # 꺼낸 파일 한자한자 확인
            tmp = file[i]
            if not tmp.isdigit() and chk == 0:  # 문자이고 head인 경우 소문자로 문자 저장
                f_name[idx][0] += tmp.lower()
                print(f_name[idx][0])
            elif not tmp.isdigit() and chk == 1:  # 숫자 다음에 또 문자가 나온 경우는 tail이니까 넣지 않고 종료
                break
            elif tmp.isdigit():  # 숫자인 경우
                chk = 1 # tail부분의 문자를 다시 head에 넣지 않기 위해 chk로 숫자 나왔다고 표시
                if num_cnt > 4:  # 숫자는 총 다섯자리니까 이를 넘으면 tail라고 판단하고 종료
                    break
                if tmp == '0' and f_name[idx][1] == '':  # 숫자 맨 처음이 0인 경우는 넣지 않고 cnt +1
                    num_cnt += 1
                    continue
                else:
                    f_name[idx][1] += tmp  # 위에 해당하지 않은 경우 숫자로 저장하기
                    num_cnt += 1


        f_name[idx][3] = idx
        if f_name[idx][1] == '':
            f_name[idx][1] = 0
        idx += 1
    print(f_name)
    f_name.sort(key=lambda x: (x[0], int(x[1]), x[3]))  # head -> 숫자 -> 인덱스 순으로 정렬
    # print(f_name)

    answer = []
    for f in f_name:
        answer.append(f[2])
    print(answer)
    return answer


# 반례 예시
files = ["a000bar.xop", "b000005", "foo010bar020.zip", "img000012345", "img1.png", "img2", "IMG02"]
solution(files)
