a, b = input(), input()
matrix = [[''] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + a[i - 1]
        else:
            if len(matrix[i - 1][j]) >= len(matrix[i][j - 1]):
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += matrix[i][j - 1]
res = matrix[-1][-1]

if len(res) == 0:
    print(0)
else:
    print(len(res))
    print(res)
