import sys

input = sys.stdin.readline
n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))

index, m_dict = 0, {}

for i in sorted(m_list):
    cnt = 0
    if i not in m_dict:
        while index < n:
            if i == n_list[index]:
                cnt += 1
                index += 1
            elif i > n_list[index]:
                index += 1
            else:
                break
        m_dict[i] = cnt
answer = [m_dict[i] for i in m_list]
print(*answer)