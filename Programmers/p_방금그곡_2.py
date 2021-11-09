def change_sharp(s):
    dict = {'C#':'H', 'D#':'I', 'F#':'J', 'G#':'K', 'A#': 'L', 'E#': 'M'}
    s += 'Z'
    idx = 0
    while True:
        if s[idx] == 'Z':
            break
        idx += 1
        if s[idx] == '#':
            s = s[:idx-1] + dict[s[idx-1:idx+1]] + s[idx+1:]
    return s[:-1]

def solution(m, musicinfos):
    m = change_sharp(m)

    results = []
    for music in musicinfos:
        music = music.split(',')
        a, b = music[1].split(':'), music[0].split(':')
        hours, mins = int(a[0])-int(b[0]), int(a[1])-int(b[1])
        music_len = hours * 60 + mins
        melody = change_sharp(music[3])
        if music_len > len(melody):
            total_info = melody * (music_len // len(melody)) + melody[:music_len % len(melody)]
        else:
            total_info = melody[:music_len]
        results.append([total_info, music[2], len(melody)])

    answer = []
    idx = 100
    for result in results:
        for j in range(len(result[0])-len(m)+1):
            if m == result[0][j:j+len(m)]:
                answer.append((len(result[0]), idx, result[1]))
                idx -= 1
                break
    if answer == []:
        return '(None)'
    answer.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return answer[0][2]
    

        

m = "ABC"
musicinfos = ["13:50,14:00,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]
print(solution(m, musicinfos))