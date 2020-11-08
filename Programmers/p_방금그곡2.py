def change(music):
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music


def solution(mm, musicinfos):
    mm = change(mm)

    answer = []
    cnt = 0
    for music in musicinfos:
        music = music.split(',')
        h = int(music[1][0:2]) - int(music[0][0:2])
        m = int(music[1][3:5]) - int(music[0][3:5])
        time = h * 60 + m

        music[3] = change(music[3])
        # print(music[3])

        m_len = len(music[3])
        q, r = divmod(time, m_len)
        music[3] = music[3] * q + music[3][:r]
        m_len = len(music[3])

        for i in range(m_len - len(mm) + 1):
            # print(f'시작 i: {i}')
            for j in range(len(mm)):
                if mm[j] != music[3][i + j]:
                    break
            else:
                if i + len(mm) < m_len + 1:
                    answer.append([music[2], len(music[3]), cnt])
                    cnt += 1
                    break
    else:
        answer.sort(key=lambda x: (-x[1], x[2]))
        if answer:
            return answer[0][0]
        return '(None)'