n, l = map(int, input().split())
position = list(map(int, input().rstrip().split()))
position.sort(reverse=True)

answer = 0
while position:
    f = position.pop()
    if position:
        while position[-1] - f <= l - 1:
            tmp = position.pop()
            if not position:
                break
    answer += 1
print(answer)