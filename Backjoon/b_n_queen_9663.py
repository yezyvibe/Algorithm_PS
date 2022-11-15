import sys
input = sys.stdin.readline

n = int(input())
queen = [0]*n
answer = 0

def check(queen, idx):
    # 그 이전 행들과 비교해서 -> 동일한 열에 둔 게 있는지 확인
    # 대각선 모두 확인
    
    for i in range(idx):
        if queen[i] == queen[idx]:
            return False # 열 번호 겹치니까 불가능
    
    for i in range(idx):
        if abs(idx - i) == abs(queen[idx] - queen[i]): 
            return False # 대각선 겹쳐서 불가능
    
    return True # 현재 열에 퀸을 둘 수 있다.



# idx는 행 번호, n은 열 번호
def dfs(queen, idx, n):
    global answer 

    if idx == n:
        answer += 1
        return

    for i in range(n):
        # 각 열마다 퀸을 두고 가능한지 확인하기
        queen[idx] = i
        if check(queen, idx):
            dfs(queen, idx+1, n) # 가능하니까 그 다음 행으로 넘어가서 탐색 진행
        queen[idx] = 0

dfs(queen, 0, n)
print(answer)