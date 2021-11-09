from collections import deque

for tc in range(int(input())):
    n, m = map(int, input().split(' '))
    lst = list(map(int, input().split(' ')))
    priority = deque([(value, idx) for idx, value in enumerate(lst)])
    cnt = 1

    while priority:
        item = priority.popleft()
        if len(priority) == 0:
            break
        else:
            max_v = max(priority)[0]
            if item[0] >= max_v:
                if item[1] == m:
                    break
                else:
                    cnt += 1
            else:
                priority.append(item)
    print(cnt)
