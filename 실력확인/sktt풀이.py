# 1.
import sys
si = sys.stdin.readline
n = int(si())
incomes = []
kills = []
for _ in range(n):
    incomes.append(list(map(int, si().split())))
    kills.append(list(map(int, si().split())))
alives = [0 for _ in range(n)]
max_saved, max_path = -1, []
def backtracking(day, alives, saved, path):
    '''
    0 ~ day-1 일까지 잘 골라왔고,
    지금 순간 배열은 alives 상태이고,
    현재까지 saved 만큼 누적되었으며,
    선택한 원소들은 path 에 저장되어 있는 상태이다.
    day ~ 4 일까지 남은 모든 시나리오를 전부 탐색해주는 함수이다.
    '''
    global max_saved, max_path
    if day == 5:
        if saved > max_saved:
            max_saved = saved
            max_path = path
        return
    for i in range(n):
        alives[i] += incomes[i][day]
        alives[i] -= kills[i][day]
        if alives[i] < 0:
            alives[i] = 0
    for i in range(n):
        val = alives[i]
        alives[i] = 0
        backtracking(day + 1, alives[:], saved + val, path + [i + 1])
        alives[i] = val
backtracking(0, alives, 0, [])
print(max_saved)
print(*max_path)

# 2.
import sys
si = sys.stdin.readline
n = int(si())
target = si().strip()
word_set = set()
for _ in range(n):
    word = si().strip()
    word_set.add(word)
dp = [-1 for _ in range(len(target) + 1)]
dp[1] = 0
for i in range(2, len(target) + 1):
    for j in range(i - 9, i):  # last word : target의 j번째 문자 ~ i번째 문자
        if j >= 1 and dp[j] != -1 and target[j - 1:i] in word_set:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp[len(target)])

# 3.
import sys
from collections import Counter
sys.setrecursionlimit(100005)
si = sys.stdin.readline
n = int(si())
move = list(map(lambda x: int(x) - 1, si().split()))
nums = list(map(int, si().split()))
visit = [False for _ in range(n)]
def traverse(idx, find_nums):
    find_nums.append(nums[idx])
    visit[idx] = True
    if not visit[move[idx]]:
        traverse(move[idx], find_nums)
ans = 0
for i in range(n):
    if visit[i]: continue
    find_nums = []
    traverse(i, find_nums)
    counter = Counter(find_nums)
    freq = max(counter.values())
    ans += len(find_nums) - freq
print(ans)
