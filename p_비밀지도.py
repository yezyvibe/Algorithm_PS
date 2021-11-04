def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(len(arr1)):
        a1 = bin(arr1[i])[2:].zfill(n)
        a2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if a1[j] == '0' and a2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer



n = 5
arr1, arr2 = [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))