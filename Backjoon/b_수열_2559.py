import sys

input = sys.stdin.readline
n, k = map(int, input().split())
n_list = list(map(int, input().split()))

# 시간초과
# max_v = 0
# for i in range(0, n-k+1):
#     k_sum = 0
#     for j in range(k):
#         k_sum += n_list[i+j]
#     max_v = max(k_sum, max_v)
# print(max_v)

tmp = sum(n_list[:k])
answer = tmp
for i in range(k, n):
    tmp += (n_list[i]- n_list[i-k])
    answer = max(answer, tmp)
print(answer)