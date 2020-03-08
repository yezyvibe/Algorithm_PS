def solution(heights):
    answer = []
    for i in range(len(heights)):
        start = heights.pop()
        print('시작')
        print(start)
        idx = 0
        for j in range(len(heights)):
            if heights[j] > start:
                idx = j+1
            else:
                if idx:
                    pass
                else:
                    idx = 0
        answer.append(idx)
    answer.reverse()
    return answer

print(solution([6,9,5,7,4]))