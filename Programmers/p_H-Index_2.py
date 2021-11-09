def solution(citations):
    n = len(citations)

    for i in range(n,-1,-1):
        print(i) # i가 h를 나타냄
        quotation_cnt = 0
        for c in citations:
            if c >= i:
                quotation_cnt += 1
                if quotation_cnt >= i:
                    return i

citations = [3,0,6,1,5]
print(solution(citations))
