def solution(citations):
    citations.sort(reverse = True)
    max_v = citations[0]
    min_v = citations[-1]

    # 세 가지 예외처리
    if min_v > len(citations): # 모든 논문의 인용 횟수가 전체 논문 개수 보다 큰 경우
        return len(citations) # 논문의 수를 리턴한다
    if max_v == 0: # 모든 논문의 인용 횟수가 0인 경우
        return 0

    # H-Index 구하는 로직
    while (max_v!=0):
        cnt = 1
        for i, c in enumerate(citations):
            if c < max_v:
                cnt = i
                break
            elif c == max_v: # 모든 논문의 인용 횟수가 동일한 경우(예외처리)
                cnt += 1
        if cnt >= max_v:
            return max_v
        max_v -= 1

citations = [5, 5, 5, 5]
print(solution(citations))