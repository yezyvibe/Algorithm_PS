def solution(genres, plays):
    total_play_times = {}
    song_dict = {}

    for i in range(len(genres)):
        if genres[i] in total_play_times:
            total_play_times[genres[i]] += plays[i]
        else:
            total_play_times[genres[i]] = plays[i]
        if genres[i] in song_dict:
            song_dict[genres[i]].append((plays[i], i))  # 재생횟수, 고유번호 순으로 저장
        else:
            song_dict[genres[i]] = [(plays[i], i)]
    for key, val in song_dict.items():
        song_dict[key] = sorted(song_dict[key], reverse=True, key= lambda x: (x[0], -x[1]))
    
    genre_list =[]
    for key, val in total_play_times.items():
        genre_list.append((val, key))
    genre_list.sort(reverse=True)

    answer = []
    for times, genre in genre_list:
        cnt = 0
        for i in range(len(song_dict[genre])):
            song_index = song_dict[genre][i][1]
            answer.append(song_index)
            cnt += 1
            if cnt == 2:
                break
    return answer

genres = ["classic","classic","classic","classic","pop"]
plays = [500,150,800,800,2500]

print(solution(genres, plays))