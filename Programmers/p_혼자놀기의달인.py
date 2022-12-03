def solution(cards):
    total = len(cards)
    visit = set()
    result = []

    idx = 0
    tmp = 0
    while idx < total:
        if idx + 1 not in visit:
            visit.add(idx+1)
            tmp += 1
            idx = cards[idx] - 1
        else:
            if tmp:
                result.append(tmp)
            idx += 1
            tmp = 0
            
    result.sort(reverse=True)
    
    return result[0] * result[1] if len(result) > 1 else 0
    
            
    