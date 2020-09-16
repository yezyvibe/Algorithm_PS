def solution(number, k):
    s = []
    cnt = 0
    for i in number:
        # 이미 k개 숫자를 삭제를 완료한 경우
        if cnt == k:
            s.append(i)
        else:
            # 처음 숫자는 먼저 넣고 시작
            if not s:
                s.append(i)
            else:
                while s:
                    if cnt == k or i <= s[-1]:
                        break
                    if i > s[-1]:
                        s.pop()
                        cnt += 1
                s.append(i)

    # 숫자 모두 넣은 후, 삭제해야 할 k가 남은 경우 처리
    while cnt != k:
        s.pop()
        cnt += 1
    return ''.join(s)


# 999, 2 => 9
# # 111119, 3 => 119