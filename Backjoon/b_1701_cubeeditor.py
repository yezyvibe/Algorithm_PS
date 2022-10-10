import sys
input = sys.stdin.readline

def make_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1] # 이전으로 돌아가기
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return max(table)

if __name__ == '__main__':
    s = input()
    answer = 0
    L = len(s)
    for idx in range(L):
        sub_str = s[idx:L]
        answer = max(answer, make_table(sub_str))
    print(answer)