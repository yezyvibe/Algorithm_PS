def solution(msg):
    # 압축 문자 사전 딕셔너리 형태로 생성
    num_dic = {}
    idx = 1
    for i in range(65, 91):
        tmp = chr(i)
        num_dic[tmp] = idx
        idx += 1
    
    # 아래부터 압축과정
    begin = 0
    next = 1
    chk = 0
    res = []
    while True:
        w = msg[begin:begin + next]
        if num_dic.get(w):
            if not chk:
                next += 1
                if begin + next > len(msg):  # 인덱스 마지막 부분 처리 
                    res.append(num_dic[w])  # 출력하고 종료
                    break
            else:
                res.append(num_dic[w])  # 출력
                num_dic[msg[begin:begin + next + 1]] = idx  # 사전 추가
                idx += 1  # 다음 사전 번호 업데이트
                begin += len(w)  # 입력에서 w 제거
                chk = 0  # chk 초기화
        else:
            next -= 1  # 사전에 없으니까 다시 이전 글자로 돌아가기
            chk = 1  # 이를 chk로 표시해두기
    return res


msg = "TOBEORNOTTOBEORTOBEORNOT"
solution(msg)
