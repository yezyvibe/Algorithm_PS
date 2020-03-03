def solution(array, commands):
    answer = []
    for i in commands:
        a = array[i[0]-1:i[1]-1]
        print(a)
        # a.sort()
        # answer.append(a[i[2]])

    return answer