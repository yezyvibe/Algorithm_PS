from itertools import permutations as permu

def checkIsPossible(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == "*":
                continue
            elif user[i][j] != banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    
    for user in permu(user_id, len(banned_id)):  # 주어진 id를 가지고 모든 가능한 제재 목록을 만든다
        if checkIsPossible(user, banned_id):
            user = set(user)
            if user not in answer:
                answer.append(user)
    return len(answer)
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))
