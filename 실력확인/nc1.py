# 문자열 중복 제거해서 dest에 알파벳 순서로 붙이기

def solution(source):
    dest = ''
    while source != '':
        removal = []
        new_source = []
        for i in range(len(source)):
            cur = source[i]
            if cur in removal:
                new_source.append(cur)
            else:
                removal.append(cur)
        removal.sort()
        dest += "".join(removal)
        source = "".join(new_source)
    return dest
