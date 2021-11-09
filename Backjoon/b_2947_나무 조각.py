namu = list(map(int, input().split(' ')))

while True:
    if namu[0] > namu[1]:
        namu[0], namu[1] = namu[1], namu[0]
        print(' '.join(map(str, namu)))
    if namu[1] > namu[2]:
        namu[1], namu[2] = namu[2], namu[1]
        print(' '.join(map(str, namu)))
    if namu[2] > namu[3]:
        namu[2], namu[3] = namu[3], namu[2]
        print(' '.join(map(str, namu)))
    if namu[3] > namu[4]:
        namu[3], namu[4] = namu[4], namu[3]
        print(' '.join(map(str, namu)))
    if namu == [1, 2, 3, 4, 5]:
        break
