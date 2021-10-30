def solution(participant, completion):
    player_dict = {}

    for i in participant:
        if i in player_dict:
            player_dict[i] += 1
        else:
            player_dict[i] = 1
    
    for i in completion:
        player_dict[i] -= 1
    
    for key, value in player_dict.items():
        if value == 1:
            return key