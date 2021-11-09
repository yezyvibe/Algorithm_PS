for tc in range(1,11):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    minNum = 1000
    idx = 0
    for i in range(100):
        if arr[0][i] == 1:
            start = i
            j = 0
            right = 0
            left = 0
            cnt = 0
            while j !=99:
                cnt +=1
                if start-1 >= 0 and arr[j][start-1] == 1 and right != 1:
                    start -= 1
                    left = 1
                    right = 0
                elif start+1 <= 99 and arr[j][start+1] == 1 and left != 1:
                    start += 1
                    left = 0
                    right = 1
                elif arr[j+1][start] == 1:
                    j += 1
                    right = 0
                    left = 0
                elif cnt > minNum:
                    break
            if cnt < minNum:
                minNum = cnt
                idx = i

    print ('#{} {}' .format(tc, idx))