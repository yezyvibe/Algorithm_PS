def solution(cards, shuffles):

    change = {}
    new_cards = [0]*(len(cards)+1)
    for i in range(len(shuffles)):
        cur = shuffles[i]
        new_cards[cur] = cards[i]
        change[i+1] = shuffles[i]
    new_cards = new_cards[1:]

    candi = []
    for i in range(len(cards)):
        if new_cards[i] != cards[i]:
            candi.append(i+1)

    idx = 0
    while idx < len(candi):
        cur = candi[idx]
        target = change[cur]
        if target in candi:
            candi.remove(target)
        idx += 1
    return len(candi)