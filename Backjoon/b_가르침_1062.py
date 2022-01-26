import sys

input = sys.stdin.readline
n, k = map(int, input().split())
words = []
for _ in range(n):
    word = input()[4:-5]
    words.append(word)
if k < 5:
    print(0)
    exit(0)
elif k == 26:
    print(n)
    exit(0)
else:
    k -= 5
alphabet = [0] * 26
for i in ('a', 'c', 'i', 'n', 't'):
    alphabet[ord(i) - ord('a')] = 1

answer = 0
def dfs(idx, cnt):
    global answer

    if cnt == k:  # 가르친 단어의 개수가 k개가 된 경우 단어 카운트 -> 최댓값 구하기
        tmp = 0
        for word in words:
            for w in word:
                if not alphabet[ord(w) - ord('a')]:
                    break
            else:
                tmp += 1
        answer = max(answer, tmp)
        return

    for i in range(idx, 26):
        # 글자 하나씩 돌려보며 최댓값 찾기
        if not alphabet[i]:
            alphabet[i] = True
            dfs(i, cnt + 1)  # 재귀
            alphabet[i] = False

dfs(0, 0)
print(answer)
