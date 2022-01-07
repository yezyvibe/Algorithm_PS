def solution(A, B):
    A.sort()
    B.sort()
    idx_a = 0
    idx_b = 0
    count = 0
    while idx_b < len(B):
        if A[idx_a] < B[idx_b]:
            idx_a += 1
            idx_b += 1
            count += 1
        else:
            idx_b += 1
    print(count)
