def check(queen, row):
    for i in range(row):
        if queen[i] == queen[row]:
            return False
        if abs(queen[i] - queen[row]) == row - i:
            return False
    return True

def search(queen, row, n):
    result = 0
    if row == n:
        return True

    for col in range(n):
        queen[row] = col # 행, 열 저장
        if check(queen, row):
            result += search(queen, row + 1, n)
    return result

def solution(n):
    queen = [0] * (n)
    return search(queen, 0, n)