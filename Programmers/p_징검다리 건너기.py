def check(stones, mid, k):
    cnt = 0
    for s in stones:
        if (s - mid) <= 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            res = 0
            break
    else:
        res = 1
    return res


def solution(stones, k):
    max_v, min_v = max(stones), min(stones)

    while True:
        mid = (max_v + min_v) // 2
        a = check(stones, mid, k)
        if min_v > max_v:
            return min_v
        if a == 1:
            min_v = mid + 1
        else:
            max_v = mid - 1