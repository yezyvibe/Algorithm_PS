from collections import defaultdict
def solution(n, results):
    win_dict = defaultdict(set)  # x를 이긴 자를 리스트로
    lose_dict = defaultdict(set) # x한테 진 자를 리스트로

    for winner, loser in results:
        lose_dict[winner].add(loser)
        win_dict[loser].add(winner)

    for i in range(1, n+1):
        for winner in win_dict[i]: # i를 이긴 애들은 i한테 진 애들도 이긴다.
            lose_dict[winner].update(lose_dict[i])
        for loser in lose_dict[i]: # i한테 진 애들은 i를 이긴 애들한테도 진다.
            win_dict[loser].update(win_dict[i])
    
    answer = 0
    for i in range(1, n+1):
        if len(win_dict[i]) + len(lose_dict[i]) == n-1:
            answer += 1
    return answer
    
n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))