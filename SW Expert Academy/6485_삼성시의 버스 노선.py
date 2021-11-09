T = int(input())
for t in range(1, T + 1):
    allStation = [0] * 5001
    n = int(input())
    for i in range(n):
        s, e = map(int, input().split())
        for bus in range(s, e + 1):
            allStation[bus] += 1
    printStation = []
    stationNum = int(input())
    for i in range(stationNum):
        printStation.append(allStation[int(input())])

    print('#{} {}'.format(t, ' '.join(map(str, printStation))))