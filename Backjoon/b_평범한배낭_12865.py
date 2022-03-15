import sys

input = sys.stdin.readline
n, k = map(int, input().split())
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]  # 물건 n개, 무게 k까지, 그리고 해당 물건의 가치를 저장함
# knapsack[n][k]는 n번째 물건까지 살펴보았을 때 무게가 k인 배낭의 최대 가치
stuff = [[0, 0]]  # 물건도 n+1개
for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재 물건을 기준으로 
        weight, value = stuff[i][0], stuff[i][1]

        if j < weight: # j 보다 weight가 크면 해당 칸에 가치를 넣을 수 없다 (무게가 무거워서 못 넣음)
            knapsack[i][j] = knapsack[i-1][j]  # 이전 물건 그대로 넣기
        else:  # 현재 물건이 작거나 같으면 가치 비교해서 계산 결과 저장
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[n][k])
