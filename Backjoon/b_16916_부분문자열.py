def make_table(pattern):
    L = len(pattern)
    table = [0] * L
    j = 0

    for i in range(1, L):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def KMP(parent, pattern):
    table = make_table(pattern)
    j = 0
    for i in range(len(parent)):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j-1]
        if parent[i] == pattern[j]:
            if j == len(pattern) - 1:
                return True
            else:
                j += 1
    return False


if __name__ == "__main__":  
    s = input()
    p = input()
    print(1 if KMP(s, p) else 0)