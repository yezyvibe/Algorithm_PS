def solution(participant, completion):
    player = {}

    for p1 in participant:
        if p1 in player.keys():
            player[p1] += 1
        else: player[p1] = 1

    for p2 in completion:
        player[p2] -= 1

    for p in player:
        if player[p] == 1:
            return p
