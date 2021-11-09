a, b = input(), input()
matrix = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])


# def s():
#     s1, s2 = input(), input()
#     dp = [0] * 1000
#     for i in range(len(s1)):
#         max_dp = 0
#         for j in range(len(s2)):
#             if max_dp < dp[j]:
#                 max_dp = dp[j]
#             elif s1[i] == s2[j]:
#                 dp[j] = max_dp + 1
#     print(max(dp))
# s()

